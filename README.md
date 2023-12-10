# License

The code in this project is distributed under the [GPL-3.0 license](LICENSE).

# postprocessing.py

## Description

Post-processing of cryo-EM maps and generation of FSC curves corrected by masking effects

> **_NOTE:_**  The code in [postprocessing.py](postprocessing.py) was adapted from [https://github.com/C-CINA/focustools](https://github.com/C-CINA/focustools).

## Usage

At a minimum, two half maps should be provided as input. To see all available options type:

<pre>
./postprocessing.py --help

Usage: postprocessing.py <half-map1> [<half-map2>] [options]


Options:
  -h, --help            show this help message and exit
  --out=postprocess     Output rootname.
  --angpix=1.0          Pixel size in Angstroems
  --fsc_threshold=0.143
                        Display the resolution at which the FSC curve crosses
                        this value.
  --lowpass="auto"      Resolution (in Angstroems) at which to low-pass filter
                        the final map. A negative value will skip low-pass
                        filtering. Default ('auto') is to low-pass at
                        resolution determined from FSC threshold.
  --highpass="auto"     Resolution (in Angstroems) at which to high-pass
                        filter the final map. Useful to to attenuate artefacts
                        such as background ramps (e.g. high-pass at 2/3 of the
                        box size). A negative value will skip high-pass
                        filtering (default).
  --mask=MyMask.mrc     A file containing the mask to be applied to the half-
                        maps before calculating the FSC. Can be combined with
                        other masking options.
  --mask_radius=0.5     Creates a soft spherical mask. This is the radius of
                        such mask, in pixels or fraction of the box size. Can
--automask_floodfill_center=0,0,0
                        Three numbers describing where the center of the
                        sphere should be placed to initialize flood-filling
                        approach in auto-masking (in pixels). Useful to mask
                        parts of the 3D map that are not close to the center.
                        Default is the middle of the box: 0,0,0. Can be
                        positive or negative.
  --automask_floodfill_fraction=0.1
                        Use this fraction of the voxels with the highest
                        densities (0.10 = top 10 percent highest densities) to
                        initialize the flood-filling algorithm. Typically
                        follows the correct map density for capsid-like or
                        hollow-center particles. Note that this is only used
                        to initialize the smart masking algorithm and has no
                        influence on the threshold, that is defined
                        independently (see options below).
  --automask_lp=14.0    Resolution (in Angstroems) at which to low-pass filter
                        the input map for auto-masking purposes. Should
                        typically be in the range of 10-20 A. However if using
                        the flood-filling approach a value in the range 5-10 A
                        might work better. Use a negative number to disable
                        this filter.
  --automask_lp_edge_width=5.0
                        Width of the cosine-edge low-pass filter to be used
                        for auto-masking (in Fourier pixels).
  --automask_lp_gauss   Use a Gaussian instead of cosine-edge low-pass filter
                        for auto-masking.
  --automask_threshold=0.02
                        Absolute threshold to generate the initial binary
                        volume in auto-masking. This has precedence over
                        --automask_fraction and --automask_sigma.
  --automask_fraction=0.1
                        Use this fraction of the voxels with the highest
                        densities (0.10 = top 10 percent highest densities) to
                        generate the initial binary volume in auto-masking.
                        This has precedence over --automask_sigma.
  --automask_sigma=1.0  Use this many standard deviations above the mean
                        density value as threshold for initial binary volume
                        generation in auto-masking. This is the default
                        option.
  --automask_expand_width=3.0
                        Width in pixels to expand the binary mask in auto-
                        masking. Useful to make the mask more generous and
                        correct for imperfections of the initial binarization.
  --automask_soft_width=6.0
                        Width in pixels to expand the binary mask in auto-
                        masking with a soft cosine edge. Very important to
                        prevent artificial correlations induced by the mask.
  --automask_optimize   Will generate a mask automatically based on the
                        automask procedure, and then tune it to optimize the
                        masked FSC corrected by High-Resolution Noise
                        Substitution (Chen et al, Ultramicroscopy 2013)
  --skip_fsc            Skip all FSC calculations, only do masking and
                        filtering stuff.
  --mw=1000.0           Molecular mass in kDa of particle or helical segment
                        comprised within the mask. Needed to calculate volume-
                        normalized Single-Particle Wiener filter (Sindelar &
                        Grigorieff, JSB 2012). If not specified, will do
                        conventional FSC weighting on the final map (Rosenthal
                        & Henderson, JMB 2003).
--mw_ignore=MW_IGNORE
                        CAUTION! EXPERIMENTAL OPTION: Molecular mass in kDa
                        present within the mask that needs to be ignored.
                        Needed to calculate an adaptation of the volume-
                        normalized Single-Particle Wiener filter (Sindelar &
                        Grigorieff, JSB 2012). Only used if --mw is also
                        specified. May be useful if your particles are
                        extracted from 2D crystals.
  --skip_fsc_weighting  Do NOT apply FSC weighting (Rosenthal & Henderson, JMB
                        2003) to the final map, nor the Single-Particle Wiener
                        filter (Sindelar & Grigorieff, JSB 2012).
  --gaussian            Apply a Gaussian (instead of cosine-edge) low-pass
                        filter to the map, with cutoffs defined by --highpass
                        and --lowpass.
  --cosine              Apply a cosine-edge low-pass filter to the final map,
                        with cutoffs defined by --highpass and --lowpass. This
                        is the default. The width of the cosine edge can be
                        specified with the option --edge_width.
  --cosine_edge_width=3.0
                        Width of the cosine-edge filter (in Fourier pixels).
                        The cutoff frequency will have a weight of 0.5, with
                        corresponding weighting above and below following the
                        cosine falloff. If set to zero, becomes a top-hat
                        filter with weighting of 1.0 at the cutoff frequency.
  --tophat              Apply a top-hat low-pass filter to the final map.
                        Equivalent to specifying --cosine with
                        --cosine_edge_width=0.
  --mtf=MTF             File containing the detector MTF for sharpening of the
                        final map.
  --auto_bfac=10.0,0.0  Estimate B-factor automatically using information in
                        this resolution range, in Angstroems (lowres,highres).
                        This works based on the Guinier plot, which should
                        ideally be a straight line from ~10.0 A and beyond
                        (Rosenthal & Henderson, JMB 2003).'If you set lowres
                        and/or maxres to -1, these values will be calculated
                        automatically. MTF and FSC weighting information are
                        employed, if not ommitted.
  --adhoc_bfac=ADHOC_BFAC
                        Apply an ad-hoc B-factor to the map (in Angstroems^2).
                        Can be positive (smoothing) or negative (sharpening).
  --whiten              Whiten the final map (that is, makes the radial
                        Amplitude Spectrum equal to 1.0 across all
                        frequencies). Should normally be used in combination
                        with the option --gaussian and --skip_fsc_weighting,
                        and also --highpass in some cases. If using this
                        option, B-factor and MTF sharpening become
                        meaningless.
  --whiten_amps         Whiten the radial Amplitude Spectrum instead of the
                        radial Power Spectrum (Amplitudes^2). Whitening
                        amplitudes seems to give a slightly more peaky (sharp)
                        map as measured by kurtosis, but the results are
                        visually almost identical. Only valid if using option
                        --whiten above.
  --randomize_below_fsc=0.8
                        If provided, will randomize phases for all Fourier
                        shells beyond the point where the FSC drops below this
                        value, to assess correlations introduced by the mask
                        by High-Resolution Noise Substitution (Chen et al,
                        Ultramicroscopy 2013). Be aware that this procedure
                        may introduce a 'dip' in the FSC curves at the
                        corresponding resolution value, but that is normal.
--randomize_beyond=10
                        If provided, will randomize phases for all Fourier
                        shells beyond this resolution shell, to assess
                        correlations introduced by the mask by High-Resolution
                        Noise Substitution (Chen et al, Ultramicroscopy 2013).
                        Be aware that this procedure may introduce a 'dip' in
                        the FSC curves at the corresponding resolution value,
                        but that is normal.
  --random_seed=123456789
                        Choose the random seed for High-Resolution Noise
                        Substitution (see option --randomize_below_fsc above)
  --flip_x              Invert handedness of input volumes along the X axis.
  --flip_y              Invert handedness of input volumes along the Y axis.
  --flip_z              Invert handedness of input volumes along the Z axis.
  --xml                 Save FSC curves also in XML format for EMDB
                        deposition.
</pre>

# par_to_bild.py

## Description

Convert a cisTEM parameter file into a .bild file for visualization in Chimera

> **_NOTE:_**  The code in [par_to_bild.py](par_to_bild.py) is based on [RELION](https://github.com/3dem/relion)'s SymList Object and [pyem](https://github.com/asarnow/pyem)'s star2bild script.

## Usage

The program takes a .par file as input and produces a .bild file ready to load in Chimera.

<pre>
par_to_bilt.py --help

usage: par_to_bild.py [-h] [--input INPUT] [--output OUTPUT] [--tomo] [--tilt_max TILT_MAX] [--healpix_order HEALPIX_ORDER] [--apix APIX] [--boxsize BOXSIZE] [--height_scale HEIGHT_SCALE] [--width_scale WIDTH_SCALE] [--occ_cutoff OCC_CUTOFF] [--sym SYM]

optional arguments:
  -h, --help            show this help message and exit
  --input INPUT         Input alignment file
  --output OUTPUT       Output .bild file
  --tomo                Refinement from tomogram tilt images
  --tilt_max TILT_MAX   max tilt angel to use from tomo data
  --healpix_order HEALPIX_ORDER
                        Healpix order (Relion convention)
  --apix APIX           Angstroms per pixel
  --boxsize BOXSIZE     Box size in pixels
  --height_scale HEIGHT_SCALE
  --width_scale WIDTH_SCALE
  --occ_cutoff OCC_CUTOFF
                        Only use the particles with occupancy above this threshold
  --sym SYM             Symmetry group to impose on distribution (Relion conventions)
</pre>