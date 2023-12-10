#!/usr/bin/env python

# bild file from Euler angles
# This script is based on RELION's SymList Object and Daniel Asarnow's pyem star2bild.py

import numpy as np
import healpy as hp
from scipy.spatial import cKDTree
import pandas as pd
import numba

import os, sys

ANGLEPSI = "psi"
ANGLETILT = "theta"
ANGLEROT = "phi"
ANGLES = [ANGLEROT, ANGLETILT, ANGLEPSI]

# symmetry list class
class SymList:
    # Point group symmetries
    pg_CI = 200
    pg_CS = 201
    pg_CN = 202
    pg_CNV = 203
    pg_CNH = 204
    pg_SN = 205
    pg_DN = 206
    pg_DNV = 207
    pg_DNH = 208
    pg_T = 209
    pg_TD = 210
    pg_TH = 211
    pg_O = 212
    pg_OH = 213
    pg_I = 214  # Default Xmipp icosahedral symmetry
    pg_IH = 215

    pg_I1 = 216  # No Crowther 222
    pg_I2 = 217  # Crowther 222 -> default in Xmipp
    pg_I3 = 218  # 52 as used by Spider
    pg_I4 = 219  # Another 52
    pg_I5 = 220  # Another another 52 (used by EMBL-matfb)

    pg_I1H = 221  # No Crowther 222, + mirror plane
    pg_I2H = 222  # Crowther 222 -> default in Xmipp + mirror plane
    pg_I3H = 223  # 52 as used by Spider + mirror plane
    pg_I4H = 224  # Another 52 + mirror plane
    pg_I5H = 225  # Another another 52 (used by EMBL-matfb) + mirror plane

    def __init__(self, sym_name):

        self.True_SymNo = 0

        self.sym_name = sym_name

    def set_matrices(self, i, L, R):
        start_row = 4 * i
        end_row = start_row + 4
        self.__L[start_row:end_row, :4] = L
        self.__R[start_row:end_row, :4] = R


    def is_sym_group(self):
        # identify symmetry group from symmetry name: C1, D2 ...

        G1 = self.sym_name[0].upper()
        G2 = self.sym_name[1].upper()

        sym_size = len(self.sym_name)

        return_true = False

        if sym_size > 2:
            G3 = self.sym_name[2].upper()
            if sym_size > 3:
                G4 = self.sym_name[3].upper()
            else:
                G4 ='\0'

        if (sym_size > 4 or sym_size<1):

            pgGroup = -1
            pgOrder = -1
            return False

        # CN
        if sym_size==2 and G1=='C' and G2.isdigit():

            pgGroup = self.pg_CN
            pgOrder=int(G2)
            return_true = True

        if sym_size==3 and G1=='C' and G2.isdigit() and G3.isdigit():

            pgGroup = self.pg_CN
            pgOrder = int(G2 + G3)
            return_true = True

        # CI
        elif sym_size==2 and G1=='C' and G2=='I': 
            pgGroup= self.pg_CI
            pgOrder = -1
            return_true = True
        # CS
        elif sym_size==2 and G1=='C' and G2=='S':

            pgGroup = self.pg_CS
            pgOrder = -1
            return_true = True

        # CNH
        elif sym_size==3 and G1=='C' and G2.isdigit() and G3=='H':
            pgGroup = self.pg_CNH
            pgOrder = int(G2)
            return_true = True
        elif sym_size==4 and G1=='C' and G2.isdigit() and G3.isdigit() and G4=='H':
            pgGroup = self.pg_CNH
            pgOrder = int(G2 + G3)
            return_true = True

        # CNV
        elif sym_size==3 and G1=='C' and G2.isdigit() and G3=='V':
            pgGroup = self.pg_CNV
            pgOrder=int(G2)
            return_true = True

        elif (sym_size==4 and G1=='C' and G2.isdigit() and G3.isdigit() and G4=='V'):

            pgGroup = self.pg_CNV
            pgOrder = int(G2 + G3)
            return_true = True

        # SN
        elif (sym_size==2 and G1=='S' and G2.isdigit() ):

            pgGroup = self.pg_SN
            pgOrder=int(G2)
            return_true = True

        elif (sym_size==3 and G1=='S' and G2.isdigit() and G3.isdigit() ):
        
            pgGroup = self.pg_SN
            pgOrder = int(G2 + G3)
            return_true = True
        
        # DN
        elif (sym_size==2 and G1=='D' and G2.isdigit() ):
        
            pgGroup = self.pg_DN
            pgOrder = int(G2)
            return_true = True
        
        if (sym_size==3 and G1=='D' and G2.isdigit() and G3.isdigit()):
        
            pgGroup = self.pg_DN
            pgOrder = int(G2 + G3)
            return_true = True
        
        # DNV
        elif (sym_size==3 and G1=='D' and G2.isdigit() and G3=='V'):
        
            pgGroup = self.pg_DNV
            pgOrder=int(G2)
            return_true = True
        
        elif (sym_size==4 and G1=='D' and G2.isdigit() and G3.isdigit() and G4=='V'):
        
            pgGroup = self.pg_DNV
            pgOrder = int(G2 + G3)
            return_true = True
        
        # DNH
        elif (sym_size==3 and G1=='D' and G2.isdigit() and G3=='H'):
        
            pgGroup = self.pg_DNH
            pgOrder=int(G2)
            return_true = True
        
        elif (sym_size==4 and G1=='D' and G2.isdigit() and G3.isdigit() and G4=='H'):
        
            pgGroup = self.pg_DNH
            pgOrder = int(G2 + G3)
            return_true = True
        
        # T
        elif (sym_size==1 and G1=='T'):
        
            pgGroup = self.pg_T
            pgOrder = -1
            return_true = True
        
        # TD
        elif (sym_size==2 and G1=='T' and G2=='D'):
        
            pgGroup = self.pg_TD
            pgOrder = -1
            return_true = True
        
        # TH
        elif (sym_size==2 and G1=='T' and G2=='H'):
        
            pgGroup = self.pg_TH
            pgOrder = -1
            return_true = True
        
        # O
        elif (sym_size==1 and G1=='O'):
        
            pgGroup = self.pg_O
            pgOrder = -1
            return_true = True
        
        # OH
        elif (sym_size==2 and G1=='O' and G2=='H'):
        
            pgGroup = self.pg_OH
            pgOrder = -1
            return_true = True
        
        # I
        elif (sym_size==1 and G1=='I'):
        
            pgGroup = self.pg_I
            pgOrder = -1
            return_true = True
        
        # I1
        elif (sym_size==2 and G1=='I' and G2=='1'):
        
            pgGroup = self.pg_I1
            pgOrder = -1
            return_true = True
        
        # I2
        elif (sym_size==2 and G1=='I' and G2=='2'):
        
            pgGroup = self.pg_I2
            pgOrder = -1
            return_true = True
        
        # I3
        elif (sym_size==2 and G1=='I' and G2=='3'):
        
            pgGroup = self.pg_I3
            pgOrder = -1
            return_true = True
        
        # I4
        elif (sym_size==2 and G1=='I' and G2=='4'):
        
            pgGroup = self.pg_I4
            pgOrder = -1
            return_true = True
        
        # I5
        elif (sym_size==2 and G1=='I' and G2=='5'):
        
            pgGroup = self.pg_I5
            pgOrder = -1
            return_true = True
        
        # IH
        elif (sym_size==2 and G1=='I' and G2=='H'):
        
            pgGroup = self.pg_IH
            pgOrder = -1
            return_true = True
        
        # I1H
        elif (sym_size==3 and G1=='I' and G2=='1' and G3=='H'):
        
            pgGroup = self.pg_I1H
            pgOrder = -1
            return_true = True
        
        # I2H
        elif (sym_size==3 and G1=='I' and G2=='2' and G3=='H'):
        
            pgGroup = self.pg_I2H
            pgOrder = -1
            return_true = True
        
        # I3H
        elif (sym_size==3 and G1=='I' and G2=='3' and G3=='H'):
        
            pgGroup = self.pg_I3H
            pgOrder = -1
            return_true = True
        
        # I4H
        elif (sym_size==3 and G1=='I' and G2=='4' and G3=='H'):
        
            pgGroup = self.pg_I4H
            pgOrder = -1
            return_true = True
        
        # I5H
        elif (sym_size==3 and G1=='I' and G2=='5' and G3=='H'):
        
            pgGroup = self.pg_I5H
            pgOrder = -1
            return_true = True
        
        return pgGroup, pgOrder, return_true


    def compute_subgroup(self):
        I = np.identity(4)
        tried = np.zeros((self.True_SymNo, self.True_SymNo), dtype=int)
        for i, j in self.found_not_tried(tried):
            
            tried[i, j] = 1
            L1, R1 = self.get_matrices(i)
            L2, R2 = self.get_matrices(j)
            newL = np.dot(L1, L2)
            newR = np.dot(R1, R2)
            new_chain_length = self.__chain_length[i] + self.__chain_length[j]
            newR3 = newR[:3, :3]

            if np.allclose(newL, I, atol=1e-6) and np.allclose(newR3, I[:3, :3], atol=1e-6):
                continue

            # Try to find it in current ones
            found = False
            symNO = self.SymNo()
            for l in range(symNO):
                L1, R1 = self.get_matrices(l)
                if np.allclose(newL, L1, atol=1e-6) and np.allclose(newR, R1, atol=1e-6):
                    found = True
                    break

            if not found:
                # Set small values to zero, if needed
                newR[np.abs(newR) < 1e-6] = 0
                newL[np.abs(newL) < 1e-6] = 0
                
                self.add_matrices(newL, newR, new_chain_length)
                # Resize the tried matrix
                tried = np.pad(tried, ((0, 1), (0, 1)), mode='constant')
                

    def found_not_tried(self, tried):
        n = 0
        i, j = 0, 0
        while n != tried.shape[0]:
            if tried[i, j] == 0 and not (i >= self.True_SymNo and j >= self.True_SymNo):
                yield i, j
            if i != n:
                i += 1
            else:
                j -= 1
                if j == -1:
                    n += 1
                    j = n
                    i = 0


    def alignWithZ(self, axis, homogeneous=False):
        if axis.size != 3:
            raise ValueError("alignWithZ: Axis is not in R3")

        # Normalize the axis
        axis = axis / np.linalg.norm(axis)

        # Compute length of the projection on YZ plane
        proj_mod = np.sqrt(axis[1]**2 + axis[2]**2)

        if homogeneous:
            result = np.zeros((4, 4))
            result[3, 3] = 1
        else:
            result = np.zeros((3, 3))

        if proj_mod > 1e-6:  # XMIPP_EQUAL_ACCURACY
            # Build Matrix result, which makes the turning axis coincident with Z
            result[0, 0] = proj_mod
            result[0, 1] = -axis[0] * axis[1] / proj_mod
            result[0, 2] = -axis[0] * axis[2] / proj_mod
            result[1, 1] = axis[2] / proj_mod
            result[1, 2] = -axis[1] / proj_mod
            result[2, 0] = axis[0]
            result[2, 1] = axis[1]
            result[2, 2] = axis[2]
        else:
            # Axis is the X axis, either positive or negative
            result[0, 2] = -1 if axis[0] > 0 else 1
            result[1, 1] = 1
            result[2, 0] = 1 if axis[0] > 0 else -1

        return result

    
    def rotationAroundZ(self, angle, homogeneous):
        """
        Create a rotation matrix for a rotation around the Z-axis
        """
        angle_rad = np.radians(angle)
        cos_ang, sin_ang = np.cos(angle_rad), np.sin(angle_rad)

        if homogeneous:
            # 4x4 homogeneous matrix
            R = np.array([
                [cos_ang, -sin_ang, 0, 0],
                [sin_ang,  cos_ang, 0, 0],
                [0,       0,       1, 0],
                [0,       0,       0, 1]
            ])
        else:
            # 3x3 matrix
            R = np.array([
                [cos_ang, -sin_ang, 0],
                [sin_ang,  cos_ang, 0],
                [0,       0,       1]
            ])

        return R


    def RotationMatrix_3D( self, angle, axis, homogeneous=False):
        if homogeneous:
            result = np.zeros((4, 4))
            result[3, 3] = 1
        else:
            result = np.zeros((3, 3))

        angle_rad = np.radians(angle)
        cosine = np.cos(angle_rad)
        sine = np.sin(angle_rad)

        if axis == 'Z':
            result[0, 0] = cosine
            result[0, 1] = -sine
            result[1, 0] = sine
            result[1, 1] = cosine
            result[2, 2] = 1
        elif axis == 'Y':
            result[0, 0] = cosine
            result[0, 2] = sine
            result[2, 0] = -sine
            result[2, 2] = cosine
            result[1, 1] = 1
        elif axis == 'X':
            result[1, 1] = cosine
            result[1, 2] = -sine
            result[2, 1] = sine
            result[2, 2] = cosine
            result[0, 0] = 1
        else:
            raise ValueError("rotation3DMatrix: Unknown axis")

        return result
    

    def Rotate_3dMatrix(self, angle, axis, homogeneous=False):
        
        A = self.alignWithZ(axis, homogeneous)
        R = self.RotationMatrix_3D(angle, "Z",  homogeneous)

        result = A.T @ R @ A

        return result
    

    def read_sym_file(self, sym_file):
        
        file_content = []
        if not os.path.isfile(sym_file):
            self.sym_name = sym_file
            
            pg_Group, pgOrder, return_true = self.is_sym_group()

            if return_true:
                
                file_content = self.fill_symmetry_class(pg_Group, pgOrder)

            else:
                print(f"Can't recognize symmetry group {sym_file}")

        else:
            # Open file
            try:
                with open(sym_file, 'r') as f:
                    for line in f:
                        if line[0] in [';', '#', '\0']:
                            continue
                        file_content.append(line.strip())

            except FileNotFoundError:
                print("Can't open symmetry file")

        self.True_SymNo = 0
        no_axis = no_mirror_planes = no_inversion_points = 0

        for line in file_content:
            tokens = line.split()
            if not tokens:
                print(f"Wrong line in symmetry file: {line}")
                continue

            if tokens[0] == 'rot_axis':
                fold = int(tokens[1])
                self.True_SymNo += (fold - 1)
                no_axis += 1
               
            elif tokens[0] == 'mirror_plane':
                self.True_SymNo += 1
                no_mirror_planes += 1
                
            elif tokens[0] == 'inversion':
                self.True_SymNo += 1
                no_inversion_points = 1

        # Initialize matrices
        self.__L = np.zeros((4 * self.True_SymNo, 4))
        self.__R = np.zeros((4 * self.True_SymNo, 4))
        self.__chain_length = np.ones(self.True_SymNo)

        # read symmetry parameters
        i = 0
        for line in file_content:
            tokens = line.split()

            if not tokens:
                continue

            if tokens[0] == "rot_axis":
                fold = int(tokens[1])
                axis = np.array([float(tokens[2]), float(tokens[3]), float(tokens[4])])
                ang_incr = 360.0 / fold

                # Identity matrices for L and R
                L = np.identity(4)
                R = np.identity(4)

                for j in range(1, fold):
                    rot_ang = ang_incr * j
                    R[0:3, 0:3] = self.Rotate_3dMatrix(rot_ang, axis)
                    # Set small values in R to zero, if needed
                    R = np.where(np.abs(R) < 1e-10, 0, R)
                    self.set_matrices(i, L, R.transpose())
                    i += 1

            elif tokens[0] == "inversion":
                # Inversion matrices for L and R
                L = np.identity(4)
                R = np.identity(4)
                R[0, 0] = -1.0
                R[1, 1] = -1.0
                R[2, 2] = -1.0
                self.set_matrices(i, L, R)
                i += 1

            elif tokens[0] == "mirror_plane":
                axis = np.array([float(tokens[1]), float(tokens[2]), float(tokens[3])])
                L = np.identity(4)
                L[2, 2] = -1.0

                # Align with Z and inverse
                A = self.alignWithZ(axis, homogeneous=False)
                A_inv = np.linalg.inv(A)
                R = A.transpose() @ L @ A_inv

                self.set_matrices(i, L, R)
                i += 1

        self.compute_subgroup()

        return pg_Group


    def fill_symmetry_class(self, pgGroup, pgOrder):

        file_content = []

        if pgGroup == self.pg_CN:
            file_content.append(f"rot_axis {pgOrder} 0 0 1")
        elif pgGroup == self.pg_CI:
            file_content.append("inversion ")
        elif pgGroup == self.pg_CS:
            file_content.append("mirror_plane 0 0 1")
        elif pgGroup == self.pg_CNV:
            file_content.append(f"rot_axis {pgOrder} 0 0 1")
            file_content.append("mirror_plane 0 1 0")
        elif pgGroup == self.pg_CNH:
            file_content.append(f"rot_axis {pgOrder} 0 0 1")
            file_content.append("mirror_plane 0 0 1")
        elif pgGroup == self.pg_SN:
            order = pgOrder // 2
            if 2 * order != pgOrder:
                raise Exception("ERROR: order for SN group must be even")
            file_content.append(f"rot_axis {order} 0 0 1")
            file_content.append("inversion ")
        elif pgGroup == self.pg_DN:
            if pgOrder > 1:
                file_content.append(f"rot_axis {pgOrder} 0 0 1")
            file_content.append("rot_axis 2 1 0 0")
        elif pgGroup == self.pg_DNV:
            if pgOrder > 1:
                file_content.append(f"rot_axis {pgOrder} 0 0 1")
            file_content.append("rot_axis 2 1 0 0")
            file_content.append("mirror_plane 1 0 0")
        elif pgGroup == self.pg_DNH:
            if pgOrder > 1:
                file_content.append(f"rot_axis {pgOrder} 0 0 1")
            file_content.append("rot_axis 2 1 0 0")
            file_content.append("mirror_plane 0 0 1")
        elif pgGroup == self.pg_T:
            file_content.append("rot_axis 3 0.0 0.0 1.0")
            file_content.append("rot_axis 2 0.0 0.816496 0.577350")
        elif pgGroup == self.pg_TD:
            file_content.append("rot_axis 3 0.0 0.0 1.0")
            file_content.append("rot_axis 2 0.0 0.816496 0.577350")
            file_content.append("mirror_plane 1.4142136 2.4494897 0.0")
        elif pgGroup == self.pg_TH:
            file_content.append("rot_axis 3 0.0 0.0 1.0")
            file_content.append("rot_axis 2 0.0 -0.816496 -0.577350")
            file_content.append("inversion")
        elif pgGroup == self.pg_O:
            file_content.append("rot_axis 3 0.5773502 0.5773502 0.5773502")
            file_content.append("rot_axis 4 0 0 1")
        elif pgGroup == self.pg_OH:
            file_content.append("rot_axis 3 0.5773502 0.5773502 0.5773502")
            file_content.append("rot_axis 4 0 0 1")
            file_content.append("mirror_plane 0 1 1")
        elif pgGroup == self.pg_I or pgGroup == self.pg_I2:
            file_content.append("rot_axis 2 0 0 1")
            file_content.append("rot_axis 5 0.525731114 0 0.850650807")
            file_content.append("rot_axis 3 0 0.356822076 0.934172364")
        elif pgGroup == self.pg_I1:
            file_content.append("rot_axis 2 1 0 0")
            file_content.append("rot_axis 5 0.85065080702670 0 -0.5257311142635")
            file_content.append("rot_axis 3 0.9341723640 0.3568220765 0")
        elif pgGroup == self.pg_I3:
            file_content.append("rot_axis 2 -0.5257311143 0 0.8506508070")
            file_content.append("rot_axis 5 0.0 0.0 1.0")
            file_content.append("rot_axis 3 -0.4911234778630044 0.3568220764705179 0.7946544753759428")
        elif pgGroup == self.pg_I4:
            file_content.append("rot_axis 2 0.5257311143 0 0.8506508070")
            file_content.append("rot_axis 5 0.8944271932547096 0 0.4472135909903704")
            file_content.append("rot_axis 3 0.4911234778630044 0.3568220764705179 0.7946544753759428")
        elif pgGroup == self.pg_I5:
            raise Exception("ERROR: Symmetry pg_I5 not implemented")
        elif pgGroup == self.pg_IH or pgGroup == self.pg_I2H:
            file_content.append("rot_axis 2 0 0 1")
            file_content.append("rot_axis 5 0.525731114 0 0.850650807")
            file_content.append("rot_axis 3 0 0.356822076 0.934172364")
            file_content.append("mirror_plane 1 0 0")
        elif pgGroup == self.pg_I1H:
            file_content.append("rot_axis 2 1 0 0")
            file_content.append("rot_axis 5 0.85065080702670 0 -0.5257311142635")
            file_content.append("rot_axis 3 0.9341723640 0.3568220765 0")
            file_content.append("mirror_plane 0 0 -1")
        elif pgGroup == self.pg_I3H:
            file_content.append("rot_axis 2 -0.5257311143 0 0.8506508070")
            file_content.append("rot_axis 5 0.0 0.0 1.0")
            file_content.append("rot_axis 3 -0.4911234778630044 0.3568220764705179 0.7946544753759428")
            file_content.append("mirror_plane 0.850650807 0 0.525731114")
        elif pgGroup == self.pg_I4H:
            file_content.append("rot_axis 2 0.5257311143 0 0.8506508070")
            file_content.append("rot_axis 5 0.8944271932547096 0 0.4472135909903704")
            file_content.append("rot_axis 3 0.4911234778630044 0.3568220764705179 0.7946544753759428")
            file_content.append("mirror_plane 0.850650807 0 -0.525731114")
        elif pgGroup == self.pg_I5H:
            raise Exception("ERROR: Symmetry pg_I5H not implemented")
        else:
            raise Exception(f"ERROR: Symmetry {self.sym_name} is not known")

        return file_content

    
    def SymNo(self):
        
        return self.__L.shape[0] // 4

    def get_matrices(self, i):
        start_row = 4 * i
        end_row = start_row + 4

        L = self.__L[start_row:end_row, :4].copy()
        R = self.__R[start_row:end_row, :4].copy()

        return L, R


    def add_matrices(self, L, R, chain_length):
        # Add new operation matrix into the object by vertial stacking
        if L.shape != (4, 4) or R.shape != (4, 4):
            raise ValueError("SymList::add_matrix: Transformation matrix is not 4x4")

        if self.True_SymNo == self.SymNo():
            self.__L = np.vstack((self.__L, np.zeros((4, 4))))
            self.__R = np.vstack((self.__R, np.zeros((4, 4))))
            self.__chain_length = np.append(self.__chain_length, 1)

        self.set_matrices(self.True_SymNo, L, R)
        self.__chain_length[-1] = chain_length
        self.True_SymNo += 1


    def Euler_matrix2angles(self, A):
        if A.shape != (3, 3):
            raise ValueError("Euler_matrix2angles: The Euler matrix is not 3x3")

        abs_sb = np.sqrt(A[0, 2]**2 + A[1, 2]**2)
        if abs_sb > 16 * np.finfo(float).eps:
            gamma = np.arctan2(A[1, 2], -A[0, 2])
            alpha = np.arctan2(A[2, 1], A[2, 0])

            if np.abs(np.sin(gamma)) < np.finfo(float).eps:
                sign_sb = np.sign(-A[0, 2] / np.cos(gamma))
            else:
                sign_sb = np.sign(A[1, 2]) if np.sin(gamma) > 0 else -np.sign(A[1, 2])

            beta = np.arctan2(sign_sb * abs_sb, A[2, 2])
        else:
            if np.sign(A[2, 2]) > 0:
                alpha = 0
                beta = 0
                gamma = np.arctan2(-A[1, 0], A[0, 0])
            else:
                alpha = 0
                beta = np.pi
                gamma = np.arctan2(A[1, 0], -A[0, 0])

        gamma = np.degrees(gamma)
        beta = np.degrees(beta)
        alpha = np.degrees(alpha)

        return alpha, beta, gamma


    def write_definition(self, sym_file : str):
        # RELION'S standard output 
        self.read_sym_file(sym_file)
        R = np.identity(3)
        print("An decoy line formated")
        print(f" ++++ Using symmetry group {self.sym_name}, with the following {self.SymNo() + 1} transformation matrices:")
        print(f" R(1)= \n{R}")
        
        for sym_id in range(self.SymNo()):
            L, R = self.get_matrices(sym_id)  
            L = L[:3, :3]
            R = R[:3, :3]
            if not np.array_equal(L, np.identity(3)):  
                print(f" L({sym_id + 2})=\n{L}")
            
            print(f" R({sym_id + 2})=\n{R}")

            alpha, beta, gamma = self.Euler_matrix2angles(R)
            print(f"     Euler angles: {alpha} {beta} {gamma}\n")


    def output_symOp(self):
        # output a list of the symmetry operation matrices
        output_list = []

        self.read_sym_file(self.sym_name)
        R = np.identity(3)
        output_list.append(R)

        for sym_id in range(self.SymNo()):
            L, R = self.get_matrices(sym_id)  
            L = L[:3, :3]
            R = R[:3, :3]
            if not np.array_equal(L, np.identity(3)):  
                output_list.append(L)
            
            output_list.append(R)

        return output_list


@numba.jit(nopython=True, nogil=True)
def rot2euler(r, out=None):
    """Decompose rotation matrix into Euler angles"""
    # assert(isrotation(r))
    # Shoemake rotation matrix decomposition algorithm with same conventions as Relion.
    # epsilon = np.finfo(np.double).eps
    epsilon = 1e-16
    r = r.reshape(-1, 9).reshape(-1, 3, 3)
    if out is None:
        out = np.zeros((len(r), 3), dtype=r.dtype)
    for i in range(len(r)):
        abs_sb = np.sqrt(r[i, 0, 2] ** 2 + r[i, 1, 2] ** 2)
        if abs_sb > 16 * epsilon:
            gamma = np.arctan2(r[i, 1, 2], -r[i, 0, 2])
            alpha = np.arctan2(r[i, 2, 1], r[i, 2, 0])
            if np.abs(np.sin(gamma)) < epsilon:
                sign_sb = np.sign(-r[i, 0, 2]) / np.cos(gamma)
            else:
                sign_sb = np.sign(r[i, 1, 2]) if np.sin(gamma) > 0 else -np.sign(r[i, 1, 2])
            beta = np.arctan2(sign_sb * abs_sb, r[i, 2, 2])
        else:
            if np.sign(r[i, 2, 2]) > 0:
                alpha = 0
                beta = 0
                gamma = np.arctan2(-r[i, 1, 0], r[i, 0, 0])
            else:
                alpha = 0
                beta = np.pi
                gamma = np.arctan2(r[i, 1, 0], -r[i, 0, 0])
        out[i, 0] = alpha
        out[i, 1] = beta
        out[i, 2] = gamma
    return out

@numba.jit(nopython=True, nogil=True, fastmath=True)
def e2r_vec(eu, out=None):
    eu = np.atleast_2d(eu)
    if out is None:
        out = np.zeros((len(eu), 3, 3))
    for i in range(len(eu)):
        ca = np.cos(eu[i, 0])
        cb = np.cos(eu[i, 1])
        cg = np.cos(eu[i, 2])
        sa = np.sin(eu[i, 0])
        sb = np.sin(eu[i, 1])
        sg = np.sin(eu[i, 2])
        cc = cb * ca
        cs = cb * sa
        sc = sb * ca
        ss = sb * sa
        out[i, 0, :] = cg * cc - sg * sa, cg * cs + sg * ca, -cg * sb
        out[i, 1, :] = -sg * cc - cg * sa, -sg * cs + cg * ca, sg * sb
        out[i, 2, :] = sc, ss, cb
    return out


def phi5(r, r2=None):
    if r2 is not None:
        r = r.dot(r2.T)
    return np.linalg.norm(np.eye(3) - r)


def relion_symmetry_group(sym):
    import io
    import sys
    old_stdout = sys.stdout
    sys.stdout = new_stdout = io.StringIO()

    sym_obj = SymList(sym)

    sym_obj.write_definition(sym)
    sys.stdout = old_stdout
    captured_output = new_stdout.getvalue()
    print(captured_output)
    lines = captured_output.split("\n")[2:]
    
    return [np.array(
        [[np.double(val) for val in l.split()] for l in lines[i:i + 3]])
        for i in range(1, len(lines), 4)]


def transform_star(df, r, t=None, inplace=False, rots=None, invert=False, rotate=True):
    """
    Transform particle angles and origins according to a rotation
    matrix (in radians) and an optional translation vector.
    The translation may also be given as the 4th column of a 3x4 matrix,
    or as a scalar distance to be applied along the axis of rotation.
    """
    ANGLEPSI = "psi"
    ANGLETILT = "theta"
    ANGLEROT = "phi"
    ANGLES = [ANGLEROT, ANGLETILT, ANGLEPSI]
    assert (r.shape[0] == 3)
    if r.shape[1] == 4 and t is None:
        t = r[:, -1]
        r = r[:, :3]
    assert (r.shape == (3, 3))
    assert t is None or np.array(t).size == 1 or len(t) == 3

    if inplace:
        newstar = df
    else:
        newstar = df.copy()

    if rots is None:
        rots = e2r_vec(np.deg2rad(df[ANGLES].values))

    if invert:
        r = r.T

    newrots = np.dot(rots, r)  # Works with 3D array and list of 2D arrays.
    if rotate:
        angles = np.rad2deg(rot2euler(newrots))
        newstar[ANGLES] = angles

    if t is not None and np.linalg.norm(t) > 0:
        if np.array(t).size == 1:
            if invert:
                tt = -(t * rots)[:, :, 2]  # Works with 3D array and list of 2D arrays.
            else:
                tt = newrots[:, :, 2] * t
        else:
            if invert:
                tt = -np.dot(rots, t)
            else:
                tt = np.dot(newrots, t)

    return newstar


def par2df(parfile, cutoff, tomo=False, tilt_max=60, angles_only=True):
    # creating pd.DataFrame with parfile 
    if angles_only:
        header = ANGLES
        # relion ANGLES = [ANGLEROT, ANGLETILT, ANGLEPSI]
        from pyp.inout.metadata import frealign_parfile
 
        pardata = frealign_parfile.Parameters.from_file(parfile).data
        # Matching relion angles order

        if tomo and tilt_max < 60:
            mask = np.logical_and(pardata[:, 11] > cutoff, np.abs(pardata[:, 17])< tilt_max)
        else:
            mask = pardata[:, 11] > cutoff

        eular_angles = pardata[mask][:, [3, 2, 1]]

        return pd.DataFrame(eular_angles, columns=header)
    

def main(args):

    # boxsize = args.boxsize
    input = args.input
    sym = args.sym
    #  healpix_order = args.healpix_order
    # apix = args.apix
    # height_scale = args.height_scale
    # width_scale = args.width_scale

    df = par2df(input, args.occ_cutoff, tomo=args.tomo, tilt_max=args.tilt_max, angles_only=True)

    if sym is not None:
        sym_obj = SymList(sym)

        args_sym = sym_obj.output_symOp()
        
        df[ANGLEPSI] = 0
        rots = e2r_vec(np.deg2rad(df.values))
        dfs = [transform_star(df[ANGLES], op, rots=rots) for op in args_sym]

        dfi = pd.concat(dfs, axis=0, keys=np.arange(len(args_sym)))
        newrots = np.array([e2r_vec(np.deg2rad(x[ANGLES].values)) for x in dfs])
        mag = np.array([phi5(r) for r in newrots.reshape(-1, 3, 3)]).reshape(len(args_sym), -1)
        idx = np.argmin(mag, axis=0)
        midx = [(i, a) for a, i in enumerate(idx)]
        df = dfi.loc[midx]

    nside = 2 ** args.healpix_order
    angular_sampling = np.sqrt(3 / np.pi) * 60 / nside
    theta, phi = hp.pix2ang(nside, np.arange(12 * nside ** 2))
    phi = np.pi - phi
    hpm = np.column_stack((np.sin(theta) * np.cos(phi),
                            np.sin(theta) * np.sin(phi),
                            np.cos(theta)))
    kdtree = cKDTree(hpm)
    st = np.sin(np.deg2rad(df[ANGLETILT]))
    ct = np.cos(np.deg2rad(df[ANGLETILT]))
    sp = np.sin(np.deg2rad(df[ANGLEROT]))
    cp = np.cos(np.deg2rad(df[ANGLEROT]))
    ptcls = np.column_stack((st * cp, st * sp, ct))
    _, idx = kdtree.query(ptcls)
    cnts = np.bincount(idx, minlength=theta.size)
    frac = cnts / np.max(cnts).astype(np.float64)
    mu = np.mean(frac)
    sigma = np.std(frac)
    color_scale = (frac - mu) / sigma
    color_scale[color_scale > 5] = 5
    color_scale[color_scale < -1] = -1
    color_scale /= 6
    color_scale += 1 / 6.
    r = args.boxsize * args.apix / 2
    rp = np.reshape(r + r * frac * args.height_scale, (-1, 1))
    base1 = hpm * r
    base2 = hpm * rp
    base1 = base1[:, [0, 1, 2]] + np.array([r]*3)
    base2 = base2[:, [0, 1, 2]] + np.array([r]*3)
    height = np.squeeze(np.abs(rp - r))
    idx = np.where(height >= 0.01)[0]
    width =  args.width_scale * np.pi * r * angular_sampling / 360
    bild = np.hstack((base1, base2, np.ones((base1.shape[0], 1)) * width))
    fmt_color = ".color %f 0 %f\n"
    fmt_cyl = ".cylinder %f %f %f %f %f %f %f\n"
    with open(args.output, "w") as f:
        for i in idx:
            f.write(fmt_color % (color_scale[i], 1 - color_scale[i]))
            f.write(fmt_cyl % tuple(bild[i]))


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="Input alignment file")
    parser.add_argument("--output", help="Output .bild file")
    parser.add_argument("--tomo", action='store_true', help="Refinement from tomogram tilt images")
    parser.add_argument("--tilt_max", help="max tilt angel to use from tomo data", type=float, default=60.0)
    parser.add_argument("--healpix_order",
                        help="Healpix order (Relion convention)", type=int,
                        default=4)
    parser.add_argument("--apix",
                        help="Angstroms per pixel",
                        type=float)
    parser.add_argument("--boxsize", help="Box size in pixels", type=int)
    parser.add_argument("--height_scale", type=float, default=0.3)
    parser.add_argument("--width_scale", type=float, default=0.5)
    parser.add_argument("--occ_cutoff",
                        help="Only use the particles with occupancy above this threshold",
                        type=float, default=50.0)
    parser.add_argument("--sym", help="Symmetry group to impose on distribution (Relion conventions)")

    main(parser.parse_args())
