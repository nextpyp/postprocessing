#!/usr/bin/env python

# The code in this file was adapted from: https://github.com/C-CINA/focustools

"""
                        GNU GENERAL PUBLIC LICENSE
                        Version 3, 29 June 2007

    Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
    Everyone is permitted to copy and distribute verbatim copies
    of this license document, but changing it is not allowed.

                                Preamble

    The GNU General Public License is a free, copyleft license for
    software and other kinds of works.

    The licenses for most software and other practical works are designed
    to take away your freedom to share and change the works.  By contrast,
    the GNU General Public License is intended to guarantee your freedom to
    share and change all versions of a program--to make sure it remains free
    software for all its users.  We, the Free Software Foundation, use the
    GNU General Public License for most of our software; it applies also to
    any other work released this way by its authors.  You can apply it to
    your programs, too.

    When we speak of free software, we are referring to freedom, not
    price.  Our General Public Licenses are designed to make sure that you
    have the freedom to distribute copies of free software (and charge for
    them if you wish), that you receive source code or can get it if you
    want it, that you can change the software or use pieces of it in new
    free programs, and that you know you can do these things.

    To protect your rights, we need to prevent others from denying you
    these rights or asking you to surrender the rights.  Therefore, you have
    certain responsibilities if you distribute copies of the software, or if
    you modify it: responsibilities to respect the freedom of others.

    For example, if you distribute copies of such a program, whether
    gratis or for a fee, you must pass on to the recipients the same
    freedoms that you received.  You must make sure that they, too, receive
    or can get the source code.  And you must show them these terms so they
    know their rights.

    Developers that use the GNU GPL protect your rights with two steps:
    (1) assert copyright on the software, and (2) offer you this License
    giving you legal permission to copy, distribute and/or modify it.

    For the developers' and authors' protection, the GPL clearly explains
    that there is no warranty for this free software.  For both users' and
    authors' sake, the GPL requires that modified versions be marked as
    changed, so that their problems will not be attributed erroneously to
    authors of previous versions.

    Some devices are designed to deny users access to install or run
    modified versions of the software inside them, although the manufacturer
    can do so.  This is fundamentally incompatible with the aim of
    protecting users' freedom to change the software.  The systematic
    pattern of such abuse occurs in the area of products for individuals to
    use, which is precisely where it is most unacceptable.  Therefore, we
    have designed this version of the GPL to prohibit the practice for those
    products.  If such problems arise substantially in other domains, we
    stand ready to extend this provision to those domains in future versions
    of the GPL, as needed to protect the freedom of users.

    Finally, every program is threatened constantly by software patents.
    States should not allow patents to restrict development and use of
    software on general-purpose computers, but in those that do, we wish to
    avoid the special danger that patents applied to a free program could
    make it effectively proprietary.  To prevent this, the GPL assures that
    patents cannot be used to render the program non-free.

    The precise terms and conditions for copying, distribution and
    modification follow.

                        TERMS AND CONDITIONS

    0. Definitions.

    "This License" refers to version 3 of the GNU General Public License.

    "Copyright" also means copyright-like laws that apply to other kinds of
    works, such as semiconductor masks.

    "The Program" refers to any copyrightable work licensed under this
    License.  Each licensee is addressed as "you".  "Licensees" and
    "recipients" may be individuals or organizations.

    To "modify" a work means to copy from or adapt all or part of the work
    in a fashion requiring copyright permission, other than the making of an
    exact copy.  The resulting work is called a "modified version" of the
    earlier work or a work "based on" the earlier work.

    A "covered work" means either the unmodified Program or a work based
    on the Program.

    To "propagate" a work means to do anything with it that, without
    permission, would make you directly or secondarily liable for
    infringement under applicable copyright law, except executing it on a
    computer or modifying a private copy.  Propagation includes copying,
    distribution (with or without modification), making available to the
    public, and in some countries other activities as well.

    To "convey" a work means any kind of propagation that enables other
    parties to make or receive copies.  Mere interaction with a user through
    a computer network, with no transfer of a copy, is not conveying.

    An interactive user interface displays "Appropriate Legal Notices"
    to the extent that it includes a convenient and prominently visible
    feature that (1) displays an appropriate copyright notice, and (2)
    tells the user that there is no warranty for the work (except to the
    extent that warranties are provided), that licensees may convey the
    work under this License, and how to view a copy of this License.  If
    the interface presents a list of user commands or options, such as a
    menu, a prominent item in the list meets this criterion.

    1. Source Code.

    The "source code" for a work means the preferred form of the work
    for making modifications to it.  "Object code" means any non-source
    form of a work.

    A "Standard Interface" means an interface that either is an official
    standard defined by a recognized standards body, or, in the case of
    interfaces specified for a particular programming language, one that
    is widely used among developers working in that language.

    The "System Libraries" of an executable work include anything, other
    than the work as a whole, that (a) is included in the normal form of
    packaging a Major Component, but which is not part of that Major
    Component, and (b) serves only to enable use of the work with that
    Major Component, or to implement a Standard Interface for which an
    implementation is available to the public in source code form.  A
    "Major Component", in this context, means a major essential component
    (kernel, window system, and so on) of the specific operating system
    (if any) on which the executable work runs, or a compiler used to
    produce the work, or an object code interpreter used to run it.

    The "Corresponding Source" for a work in object code form means all
    the source code needed to generate, install, and (for an executable
    work) run the object code and to modify the work, including scripts to
    control those activities.  However, it does not include the work's
    System Libraries, or general-purpose tools or generally available free
    programs which are used unmodified in performing those activities but
    which are not part of the work.  For example, Corresponding Source
    includes interface definition files associated with source files for
    the work, and the source code for shared libraries and dynamically
    linked subprograms that the work is specifically designed to require,
    such as by intimate data communication or control flow between those
    subprograms and other parts of the work.

    The Corresponding Source need not include anything that users
    can regenerate automatically from other parts of the Corresponding
    Source.

    The Corresponding Source for a work in source code form is that
    same work.

    2. Basic Permissions.

    All rights granted under this License are granted for the term of
    copyright on the Program, and are irrevocable provided the stated
    conditions are met.  This License explicitly affirms your unlimited
    permission to run the unmodified Program.  The output from running a
    covered work is covered by this License only if the output, given its
    content, constitutes a covered work.  This License acknowledges your
    rights of fair use or other equivalent, as provided by copyright law.

    You may make, run and propagate covered works that you do not
    convey, without conditions so long as your license otherwise remains
    in force.  You may convey covered works to others for the sole purpose
    of having them make modifications exclusively for you, or provide you
    with facilities for running those works, provided that you comply with
    the terms of this License in conveying all material for which you do
    not control copyright.  Those thus making or running the covered works
    for you must do so exclusively on your behalf, under your direction
    and control, on terms that prohibit them from making any copies of
    your copyrighted material outside their relationship with you.

    Conveying under any other circumstances is permitted solely under
    the conditions stated below.  Sublicensing is not allowed; section 10
    makes it unnecessary.

    3. Protecting Users' Legal Rights From Anti-Circumvention Law.

    No covered work shall be deemed part of an effective technological
    measure under any applicable law fulfilling obligations under article
    11 of the WIPO copyright treaty adopted on 20 December 1996, or
    similar laws prohibiting or restricting circumvention of such
    measures.

    When you convey a covered work, you waive any legal power to forbid
    circumvention of technological measures to the extent such circumvention
    is effected by exercising rights under this License with respect to
    the covered work, and you disclaim any intention to limit operation or
    modification of the work as a means of enforcing, against the work's
    users, your or third parties' legal rights to forbid circumvention of
    technological measures.

    4. Conveying Verbatim Copies.

    You may convey verbatim copies of the Program's source code as you
    receive it, in any medium, provided that you conspicuously and
    appropriately publish on each copy an appropriate copyright notice;
    keep intact all notices stating that this License and any
    non-permissive terms added in accord with section 7 apply to the code;
    keep intact all notices of the absence of any warranty; and give all
    recipients a copy of this License along with the Program.

    You may charge any price or no price for each copy that you convey,
    and you may offer support or warranty protection for a fee.

    5. Conveying Modified Source Versions.

    You may convey a work based on the Program, or the modifications to
    produce it from the Program, in the form of source code under the
    terms of section 4, provided that you also meet all of these conditions:

        a) The work must carry prominent notices stating that you modified
        it, and giving a relevant date.

        b) The work must carry prominent notices stating that it is
        released under this License and any conditions added under section
        7.  This requirement modifies the requirement in section 4 to
        "keep intact all notices".

        c) You must license the entire work, as a whole, under this
        License to anyone who comes into possession of a copy.  This
        License will therefore apply, along with any applicable section 7
        additional terms, to the whole of the work, and all its parts,
        regardless of how they are packaged.  This License gives no
        permission to license the work in any other way, but it does not
        invalidate such permission if you have separately received it.

        d) If the work has interactive user interfaces, each must display
        Appropriate Legal Notices; however, if the Program has interactive
        interfaces that do not display Appropriate Legal Notices, your
        work need not make them do so.

    A compilation of a covered work with other separate and independent
    works, which are not by their nature extensions of the covered work,
    and which are not combined with it such as to form a larger program,
    in or on a volume of a storage or distribution medium, is called an
    "aggregate" if the compilation and its resulting copyright are not
    used to limit the access or legal rights of the compilation's users
    beyond what the individual works permit.  Inclusion of a covered work
    in an aggregate does not cause this License to apply to the other
    parts of the aggregate.

    6. Conveying Non-Source Forms.

    You may convey a covered work in object code form under the terms
    of sections 4 and 5, provided that you also convey the
    machine-readable Corresponding Source under the terms of this License,
    in one of these ways:

        a) Convey the object code in, or embodied in, a physical product
        (including a physical distribution medium), accompanied by the
        Corresponding Source fixed on a durable physical medium
        customarily used for software interchange.

        b) Convey the object code in, or embodied in, a physical product
        (including a physical distribution medium), accompanied by a
        written offer, valid for at least three years and valid for as
        long as you offer spare parts or customer support for that product
        model, to give anyone who possesses the object code either (1) a
        copy of the Corresponding Source for all the software in the
        product that is covered by this License, on a durable physical
        medium customarily used for software interchange, for a price no
        more than your reasonable cost of physically performing this
        conveying of source, or (2) access to copy the
        Corresponding Source from a network server at no charge.

        c) Convey individual copies of the object code with a copy of the
        written offer to provide the Corresponding Source.  This
        alternative is allowed only occasionally and noncommercially, and
        only if you received the object code with such an offer, in accord
        with subsection 6b.

        d) Convey the object code by offering access from a designated
        place (gratis or for a charge), and offer equivalent access to the
        Corresponding Source in the same way through the same place at no
        further charge.  You need not require recipients to copy the
        Corresponding Source along with the object code.  If the place to
        copy the object code is a network server, the Corresponding Source
        may be on a different server (operated by you or a third party)
        that supports equivalent copying facilities, provided you maintain
        clear directions next to the object code saying where to find the
        Corresponding Source.  Regardless of what server hosts the
        Corresponding Source, you remain obligated to ensure that it is
        available for as long as needed to satisfy these requirements.

        e) Convey the object code using peer-to-peer transmission, provided
        you inform other peers where the object code and Corresponding
        Source of the work are being offered to the general public at no
        charge under subsection 6d.

    A separable portion of the object code, whose source code is excluded
    from the Corresponding Source as a System Library, need not be
    included in conveying the object code work.

    A "User Product" is either (1) a "consumer product", which means any
    tangible personal property which is normally used for personal, family,
    or household purposes, or (2) anything designed or sold for incorporation
    into a dwelling.  In determining whether a product is a consumer product,
    doubtful cases shall be resolved in favor of coverage.  For a particular
    product received by a particular user, "normally used" refers to a
    typical or common use of that class of product, regardless of the status
    of the particular user or of the way in which the particular user
    actually uses, or expects or is expected to use, the product.  A product
    is a consumer product regardless of whether the product has substantial
    commercial, industrial or non-consumer uses, unless such uses represent
    the only significant mode of use of the product.

    "Installation Information" for a User Product means any methods,
    procedures, authorization keys, or other information required to install
    and execute modified versions of a covered work in that User Product from
    a modified version of its Corresponding Source.  The information must
    suffice to ensure that the continued functioning of the modified object
    code is in no case prevented or interfered with solely because
    modification has been made.

    If you convey an object code work under this section in, or with, or
    specifically for use in, a User Product, and the conveying occurs as
    part of a transaction in which the right of possession and use of the
    User Product is transferred to the recipient in perpetuity or for a
    fixed term (regardless of how the transaction is characterized), the
    Corresponding Source conveyed under this section must be accompanied
    by the Installation Information.  But this requirement does not apply
    if neither you nor any third party retains the ability to install
    modified object code on the User Product (for example, the work has
    been installed in ROM).

    The requirement to provide Installation Information does not include a
    requirement to continue to provide support service, warranty, or updates
    for a work that has been modified or installed by the recipient, or for
    the User Product in which it has been modified or installed.  Access to a
    network may be denied when the modification itself materially and
    adversely affects the operation of the network or violates the rules and
    protocols for communication across the network.

    Corresponding Source conveyed, and Installation Information provided,
    in accord with this section must be in a format that is publicly
    documented (and with an implementation available to the public in
    source code form), and must require no special password or key for
    unpacking, reading or copying.

    7. Additional Terms.

    "Additional permissions" are terms that supplement the terms of this
    License by making exceptions from one or more of its conditions.
    Additional permissions that are applicable to the entire Program shall
    be treated as though they were included in this License, to the extent
    that they are valid under applicable law.  If additional permissions
    apply only to part of the Program, that part may be used separately
    under those permissions, but the entire Program remains governed by
    this License without regard to the additional permissions.

    When you convey a copy of a covered work, you may at your option
    remove any additional permissions from that copy, or from any part of
    it.  (Additional permissions may be written to require their own
    removal in certain cases when you modify the work.)  You may place
    additional permissions on material, added by you to a covered work,
    for which you have or can give appropriate copyright permission.

    Notwithstanding any other provision of this License, for material you
    add to a covered work, you may (if authorized by the copyright holders of
    that material) supplement the terms of this License with terms:

        a) Disclaiming warranty or limiting liability differently from the
        terms of sections 15 and 16 of this License; or

        b) Requiring preservation of specified reasonable legal notices or
        author attributions in that material or in the Appropriate Legal
        Notices displayed by works containing it; or

        c) Prohibiting misrepresentation of the origin of that material, or
        requiring that modified versions of such material be marked in
        reasonable ways as different from the original version; or

        d) Limiting the use for publicity purposes of names of licensors or
        authors of the material; or

        e) Declining to grant rights under trademark law for use of some
        trade names, trademarks, or service marks; or

        f) Requiring indemnification of licensors and authors of that
        material by anyone who conveys the material (or modified versions of
        it) with contractual assumptions of liability to the recipient, for
        any liability that these contractual assumptions directly impose on
        those licensors and authors.

    All other non-permissive additional terms are considered "further
    restrictions" within the meaning of section 10.  If the Program as you
    received it, or any part of it, contains a notice stating that it is
    governed by this License along with a term that is a further
    restriction, you may remove that term.  If a license document contains
    a further restriction but permits relicensing or conveying under this
    License, you may add to a covered work material governed by the terms
    of that license document, provided that the further restriction does
    not survive such relicensing or conveying.

    If you add terms to a covered work in accord with this section, you
    must place, in the relevant source files, a statement of the
    additional terms that apply to those files, or a notice indicating
    where to find the applicable terms.

    Additional terms, permissive or non-permissive, may be stated in the
    form of a separately written license, or stated as exceptions;
    the above requirements apply either way.

    8. Termination.

    You may not propagate or modify a covered work except as expressly
    provided under this License.  Any attempt otherwise to propagate or
    modify it is void, and will automatically terminate your rights under
    this License (including any patent licenses granted under the third
    paragraph of section 11).

    However, if you cease all violation of this License, then your
    license from a particular copyright holder is reinstated (a)
    provisionally, unless and until the copyright holder explicitly and
    finally terminates your license, and (b) permanently, if the copyright
    holder fails to notify you of the violation by some reasonable means
    prior to 60 days after the cessation.

    Moreover, your license from a particular copyright holder is
    reinstated permanently if the copyright holder notifies you of the
    violation by some reasonable means, this is the first time you have
    received notice of violation of this License (for any work) from that
    copyright holder, and you cure the violation prior to 30 days after
    your receipt of the notice.

    Termination of your rights under this section does not terminate the
    licenses of parties who have received copies or rights from you under
    this License.  If your rights have been terminated and not permanently
    reinstated, you do not qualify to receive new licenses for the same
    material under section 10.

    9. Acceptance Not Required for Having Copies.

    You are not required to accept this License in order to receive or
    run a copy of the Program.  Ancillary propagation of a covered work
    occurring solely as a consequence of using peer-to-peer transmission
    to receive a copy likewise does not require acceptance.  However,
    nothing other than this License grants you permission to propagate or
    modify any covered work.  These actions infringe copyright if you do
    not accept this License.  Therefore, by modifying or propagating a
    covered work, you indicate your acceptance of this License to do so.

    10. Automatic Licensing of Downstream Recipients.

    Each time you convey a covered work, the recipient automatically
    receives a license from the original licensors, to run, modify and
    propagate that work, subject to this License.  You are not responsible
    for enforcing compliance by third parties with this License.

    An "entity transaction" is a transaction transferring control of an
    organization, or substantially all assets of one, or subdividing an
    organization, or merging organizations.  If propagation of a covered
    work results from an entity transaction, each party to that
    transaction who receives a copy of the work also receives whatever
    licenses to the work the party's predecessor in interest had or could
    give under the previous paragraph, plus a right to possession of the
    Corresponding Source of the work from the predecessor in interest, if
    the predecessor has it or can get it with reasonable efforts.

    You may not impose any further restrictions on the exercise of the
    rights granted or affirmed under this License.  For example, you may
    not impose a license fee, royalty, or other charge for exercise of
    rights granted under this License, and you may not initiate litigation
    (including a cross-claim or counterclaim in a lawsuit) alleging that
    any patent claim is infringed by making, using, selling, offering for
    sale, or importing the Program or any portion of it.

    11. Patents.

    A "contributor" is a copyright holder who authorizes use under this
    License of the Program or a work on which the Program is based.  The
    work thus licensed is called the contributor's "contributor version".

    A contributor's "essential patent claims" are all patent claims
    owned or controlled by the contributor, whether already acquired or
    hereafter acquired, that would be infringed by some manner, permitted
    by this License, of making, using, or selling its contributor version,
    but do not include claims that would be infringed only as a
    consequence of further modification of the contributor version.  For
    purposes of this definition, "control" includes the right to grant
    patent sublicenses in a manner consistent with the requirements of
    this License.

    Each contributor grants you a non-exclusive, worldwide, royalty-free
    patent license under the contributor's essential patent claims, to
    make, use, sell, offer for sale, import and otherwise run, modify and
    propagate the contents of its contributor version.

    In the following three paragraphs, a "patent license" is any express
    agreement or commitment, however denominated, not to enforce a patent
    (such as an express permission to practice a patent or covenant not to
    sue for patent infringement).  To "grant" such a patent license to a
    party means to make such an agreement or commitment not to enforce a
    patent against the party.

    If you convey a covered work, knowingly relying on a patent license,
    and the Corresponding Source of the work is not available for anyone
    to copy, free of charge and under the terms of this License, through a
    publicly available network server or other readily accessible means,
    then you must either (1) cause the Corresponding Source to be so
    available, or (2) arrange to deprive yourself of the benefit of the
    patent license for this particular work, or (3) arrange, in a manner
    consistent with the requirements of this License, to extend the patent
    license to downstream recipients.  "Knowingly relying" means you have
    actual knowledge that, but for the patent license, your conveying the
    covered work in a country, or your recipient's use of the covered work
    in a country, would infringe one or more identifiable patents in that
    country that you have reason to believe are valid.

    If, pursuant to or in connection with a single transaction or
    arrangement, you convey, or propagate by procuring conveyance of, a
    covered work, and grant a patent license to some of the parties
    receiving the covered work authorizing them to use, propagate, modify
    or convey a specific copy of the covered work, then the patent license
    you grant is automatically extended to all recipients of the covered
    work and works based on it.

    A patent license is "discriminatory" if it does not include within
    the scope of its coverage, prohibits the exercise of, or is
    conditioned on the non-exercise of one or more of the rights that are
    specifically granted under this License.  You may not convey a covered
    work if you are a party to an arrangement with a third party that is
    in the business of distributing software, under which you make payment
    to the third party based on the extent of your activity of conveying
    the work, and under which the third party grants, to any of the
    parties who would receive the covered work from you, a discriminatory
    patent license (a) in connection with copies of the covered work
    conveyed by you (or copies made from those copies), or (b) primarily
    for and in connection with specific products or compilations that
    contain the covered work, unless you entered into that arrangement,
    or that patent license was granted, prior to 28 March 2007.

    Nothing in this License shall be construed as excluding or limiting
    any implied license or other defenses to infringement that may
    otherwise be available to you under applicable patent law.

    12. No Surrender of Others' Freedom.

    If conditions are imposed on you (whether by court order, agreement or
    otherwise) that contradict the conditions of this License, they do not
    excuse you from the conditions of this License.  If you cannot convey a
    covered work so as to satisfy simultaneously your obligations under this
    License and any other pertinent obligations, then as a consequence you may
    not convey it at all.  For example, if you agree to terms that obligate you
    to collect a royalty for further conveying from those to whom you convey
    the Program, the only way you could satisfy both those terms and this
    License would be to refrain entirely from conveying the Program.

    13. Use with the GNU Affero General Public License.

    Notwithstanding any other provision of this License, you have
    permission to link or combine any covered work with a work licensed
    under version 3 of the GNU Affero General Public License into a single
    combined work, and to convey the resulting work.  The terms of this
    License will continue to apply to the part which is the covered work,
    but the special requirements of the GNU Affero General Public License,
    section 13, concerning interaction through a network will apply to the
    combination as such.

    14. Revised Versions of this License.

    The Free Software Foundation may publish revised and/or new versions of
    the GNU General Public License from time to time.  Such new versions will
    be similar in spirit to the present version, but may differ in detail to
    address new problems or concerns.

    Each version is given a distinguishing version number.  If the
    Program specifies that a certain numbered version of the GNU General
    Public License "or any later version" applies to it, you have the
    option of following the terms and conditions either of that numbered
    version or of any later version published by the Free Software
    Foundation.  If the Program does not specify a version number of the
    GNU General Public License, you may choose any version ever published
    by the Free Software Foundation.

    If the Program specifies that a proxy can decide which future
    versions of the GNU General Public License can be used, that proxy's
    public statement of acceptance of a version permanently authorizes you
    to choose that version for the Program.

    Later license versions may give you additional or different
    permissions.  However, no additional obligations are imposed on any
    author or copyright holder as a result of your choosing to follow a
    later version.

    15. Disclaimer of Warranty.

    THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
    APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
    HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
    OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
    THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
    PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
    IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
    ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

    16. Limitation of Liability.

    IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
    WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS
    THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY
    GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE
    USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF
    DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD
    PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),
    EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF
    SUCH DAMAGES.

    17. Interpretation of Sections 15 and 16.

    If the disclaimer of warranty and limitation of liability provided
    above cannot be given local legal effect according to their terms,
    reviewing courts shall apply local law that most closely approximates
    an absolute waiver of all civil liability in connection with the
    Program, unless a warranty or assumption of liability accompanies a
    copy of the Program in return for a fee.

                        END OF TERMS AND CONDITIONS

                How to Apply These Terms to Your New Programs

    If you develop a new program, and you want it to be of the greatest
    possible use to the public, the best way to achieve this is to make it
    free software which everyone can redistribute and change under these terms.

    To do so, attach the following notices to the program.  It is safest
    to attach them to the start of each source file to most effectively
    state the exclusion of warranty; and each file should have at least
    the "copyright" line and a pointer to where the full notice is found.

        <one line to give the program's name and a brief idea of what it does.>
        Copyright (C) <year>  <name of author>

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.

        You should have received a copy of the GNU General Public License
        along with this program.  If not, see <https://www.gnu.org/licenses/>.

    Also add information on how to contact you by electronic and paper mail.

    If the program does terminal interaction, make it output a short
    notice like this when it starts in an interactive mode:

        <program>  Copyright (C) <year>  <name of author>
        This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
        This is free software, and you are welcome to redistribute it
        under certain conditions; type `show c' for details.

    The hypothetical commands `show w' and `show c' should show the appropriate
    parts of the General Public License.  Of course, your program's commands
    might be different; for a GUI interface, you would use an "about box".

    You should also get your employer (if you work as a programmer) or school,
    if any, to sign a "copyright disclaimer" for the program, if necessary.
    For more information on this, and how to apply and follow the GNU GPL, see
    <https://www.gnu.org/licenses/>.

    The GNU General Public License does not permit incorporating your program
    into proprietary programs.  If your program is a subroutine library, you
    may consider it more useful to permit linking proprietary applications with
    the library.  If this is what you want to do, use the GNU Lesser General
    Public License instead of this License.  But first, please read
    <https://www.gnu.org/licenses/why-not-lgpl.html>.
"""

import sys
import os
import numpy as np
from pyp.inout.image import mrc
from optparse import OptionParser
import numexpr as ne
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

from pyp.system.logging import initialize_pyp_logger
from pyp.utils import get_relative_path
relative_path = str(get_relative_path(__file__))
logger = initialize_pyp_logger(log_name=relative_path)

pi = np.pi  # global PI

def RadialIndices(imsize=[100, 100], rounding=True, normalize=False, rfft=False, xyz=[0, 0, 0], nozero=True):
    """Returns radius and angles for each pixel (or voxel) in a 2D image or 3D volume of shape = imsize

    Parameters
    ----------
    imsize : list, optional
        _description_, by default [100, 100]
    rounding : bool, optional
        Rounding is to ensure "perfect" radial symmetry, desirable in some applications, by default True
    normalize : bool, optional
        Normalize=True will normalize the radius to values between 0.0 and 1.0, by default False
    rfft : bool, optional
        rfft=True will return only half of the radial indices in a way that is compliant with the FFT of real inputs, by default False
    xyz : list, optional
        _description_, by default [0, 0, 0]
    nozero : bool, optional
        _description_, by default True
    """

    imsize = np.array(imsize)

    if np.isscalar(imsize):

        imsize = [imsize, imsize]

    if len(imsize) > 3:

        raise ValueError(
            "Object should have 2 or 3 dimensions: len(imsize) = %d " % len(imsize))

    xyz = np.flipud(xyz)

    m = np.mod(imsize, 2)  # Check if dimensions are odd or even

    if len(imsize) == 1:

        if not rfft:

            xmesh = np.mgrid[-imsize[0] // 2 + m[0] -
                             xyz[0]:(imsize[0] - 1) // 2 + 1 - xyz[0]]

        else:

            xmesh = np.mgrid[0 - xyz[0]:imsize[0] // 2 + 1 - xyz[0]]

        rmesh = ne.evaluate("sqrt(xmesh * xmesh)")

        amesh = np.zeros(xmesh.shape)

        n = 1  # Normalization factor

    if len(imsize) == 2:

        # The definition below is consistent with numpy np.fft.fftfreq and np.fft.rfftfreq:

        if not rfft:

            [xmesh, ymesh] = np.mgrid[-imsize[0] // 2 + m[0] - xyz[0]
                :(imsize[0] - 1) // 2 + 1 - xyz[0], -imsize[1] // 2 + m[1] - xyz[1]:(imsize[1] - 1) // 2 + 1 - xyz[1]]

        else:

            [xmesh, ymesh] = np.mgrid[-imsize[0] // 2 + m[0] - xyz[0]
                :(imsize[0] - 1) // 2 + 1 - xyz[0], 0 - xyz[1]:imsize[1] // 2 + 1 - xyz[1]]
            xmesh = np.fft.ifftshift(xmesh)

        rmesh = ne.evaluate("sqrt(xmesh * xmesh + ymesh * ymesh)")

        amesh = ne.evaluate("arctan2(ymesh, xmesh)")

        n = 2  # Normalization factor

    if len(imsize) == 3:

        if not rfft:

            [xmesh, ymesh, zmesh] = np.mgrid[-imsize[0] // 2 + m[0] - xyz[0]:(imsize[0] - 1) // 2 + 1 - xyz[0], -imsize[1] // 2 + m[1] - xyz[1]:(
                imsize[1] - 1) // 2 + 1 - xyz[1], -imsize[2] // 2 + m[2] - xyz[2]:(imsize[2] - 1) // 2 + 1 - xyz[2]]

        else:

            [xmesh, ymesh, zmesh] = np.mgrid[-imsize[0] // 2 + m[0] - xyz[0]:(imsize[0] - 1) // 2 + 1 - xyz[0], -imsize[1] // 2 + m[1] - xyz[1]:(
                imsize[1] - 1) // 2 + 1 - xyz[1], 0 - xyz[2]:imsize[2] // 2 + 1 - xyz[2]]
            xmesh = np.fft.ifftshift(xmesh)
            ymesh = np.fft.ifftshift(ymesh)

        rmesh = ne.evaluate(
            "sqrt(xmesh * xmesh + ymesh * ymesh + zmesh * zmesh)")

        amesh = ne.evaluate("arccos(zmesh / rmesh)")

        n = 3  # Normalization factor

    if rounding:

        rmesh = np.round(rmesh)

    if normalize:

        a = np.sum(imsize * imsize)
        ne.evaluate("rmesh / (sqrt(a) / sqrt(n))", out=rmesh)

    if nozero:

        # Replaces the "zero radius" by a small value to prevent division by zero in other programs
        idx = ne.evaluate("rmesh == 0")
        rmesh[idx] = 1e-3

    return rmesh, np.nan_to_num(amesh)


def RotationalAverage(img, nomean=False):
    # Compute the rotational average of a 2D image or 3D volume
    # 'nomean' is a switch to compute the Rotational Sum instead of the Rotational Average

    rmesh = RadialIndices(img.shape, rounding=True)[0]

    rotavg = np.zeros(img.shape)

    idx = np.zeros(rmesh.shape, dtype='bool')

    if nomean:

        for r in np.unique(rmesh):

            ne.evaluate("rmesh == r", out=idx)
            a = img[idx]
            rotavg[idx] = np.sum(a)

        return rotavg

    else:

        nvoxels = np.bincount(rmesh.ravel().astype('int32'))

        for j, r in enumerate(np.unique(rmesh)):

            ne.evaluate("rmesh == r", out=idx)
            a = img[idx]
            b = nvoxels[j]
            rotavg[idx] = np.sum(a) / b

        return rotavg


def RadialProfile(img, amps=False):
    # Compute the 1D radial profile of a 2D image or 3D volume:
    # 'amps' is a flag to tell whether we want a radial profile of the Fourier amplitudes

    orgshape = img.shape

    if amps:

        img = np.abs(np.fft.rfftn(img, norm='ortho'))
        rfft = True

    else:

        rfft = False

    rmesh = RadialIndices(orgshape, rounding=True, rfft=rfft)[
        0].ravel().astype('int32')
    profile = np.bincount(rmesh, img.ravel()) / np.bincount(rmesh)
    return profile


def RadialFilter(img, filt, return_filter=False):
    # Given a list of factors 'filt', radially multiplies the Fourier Transform of 'img' by the corresponding term in 'filt'

    rmesh = RadialIndices(img.shape, rounding=True, rfft=True)[0].astype('int')

    ft = np.fft.rfftn(img).astype('complex128')
    # j = 0
    idx = np.zeros(rmesh.shape, dtype='bool')
    filtmat = np.zeros(rmesh.shape)
    for j, r in enumerate(np.unique(rmesh)):
        ne.evaluate("rmesh == r", out=idx)
        filtmat[idx] = filt[j]

    ne.evaluate("ft * filtmat", out=ft)

    if not return_filter:

        return np.fft.irfftn(ft, s=img.shape)

    else:

        return np.fft.irfftn(ft, s=img.shape), filtmat


def SoftMask(imsize=[100, 100], radius=0.5, width=6.0, rounding=False, xyz=[0, 0, 0], rfft=False):
    # Generates a circular or spherical mask with a soft cosine edge
    # If rfft==True, the output shape will not be imsize, be the shape of an rfft of input shape imsize

    if np.isscalar(imsize):

        imsize = [imsize, imsize]

    if len(imsize) > 3:

        raise ValueError(
            "Object should have 2 or 3 dimensions: len(imsize) = %d " % len(imsize))

    rmesh = RadialIndices(imsize, rounding=rounding, xyz=xyz, rfft=rfft)[0]

    if width < 0.0:

        width = 0.0

    if width > 0.0 and width < 1.0:

        width = 0.5 * width * np.min(imsize)

    if radius > 0.0 and radius < 1.0:

        radius = radius * np.min(imsize)

        radius *= 0.5

    if (radius < 0.0) or (np.min(imsize) < radius * 2):

        radius = 0.5 * (np.min(imsize) - float(width) / 2)

    rii = radius + width / 2
    rih = radius - width / 2

    mask = np.zeros(rmesh.shape)

    fill_idx = ne.evaluate("rmesh <= rih")
    mask[fill_idx] = 1.0

    rih_idx = ne.evaluate("rmesh > rih")
    rii_idx = ne.evaluate("rmesh <= rii")
    edge_idx = ne.evaluate("rih_idx & rii_idx")

    a = rmesh[edge_idx]
    ne.evaluate("( 1.0 + cos(pi * (a - rih) / (width))) / 2.0",
                out=mask[edge_idx])
    return mask


def AutoMask(img, apix=1.0, lp=-1, gaussian=False, cosine=True, cosine_edge_width=3.0, absolute_threshold=None, fraction_threshold=None, sigma_threshold=1.0, expand_width=3.0, expand_soft_width=3.0, floodfill_rad=None, floodfill_xyz=[0, 0, 0], floodfill_fraction=None, verbose=False):

    # First we low-pass filter the volume with a Gaussian or Cosine-edge filter:
    if gaussian:

        imglp = FilterGauss(img, apix=apix, lp=lp)
        filter_type = "Gaussian."

    else:

        imglp = FilterCosine(img, apix=apix, lp=lp, width=cosine_edge_width)
        filter_type = "cosine-edge across %.1f Fourier voxels" % cosine_edge_width

    # Then we define a threshold for binarization of the low-pass filtered map:
    if absolute_threshold != None:

        thr = absolute_threshold  # Simply take a user-specified value as threshold
        method = "absolute value"

    elif fraction_threshold != None:

        # Binarize the voxels with the top fraction_threshold densities
        thr = np.percentile(imglp, 100.0 - 100.0 * fraction_threshold)
        method = "highest %.1f percent of densities" % (
            fraction_threshold * 100)

    elif sigma_threshold != None:

        # Or define as threshold a multiple of standard deviations above the mean density value
        thr = imglp.mean() + sigma_threshold * imglp.std()

        method = "%.3f standard deviations above the mean" % sigma_threshold

    else:

        thr = 0.0

    if verbose:

        logger.info("Input volume will be low-pass filtered at %.2f A by a %s" %
              (lp, filter_type))
        logger.info("Input volume stats before filtering: Range=[%.2f, %.3f], Median=%.3f, Mean=%.3f, Std=%.3f" %
              (img.min(), img.max(), np.median(img), img.mean(), img.std()))
        logger.info("Input volume stats after filtering: Range=[%.3f, %.3f], Median=%.3f, Mean=%.3f, Std=%.3f" %
              (imglp.min(), imglp.max(), np.median(imglp), imglp.mean(), imglp.std()))
        logger.info("Thresholding method: %s" % method)
        logger.info("Threshold for initial binarization: %.6f" % thr)
        logger.info("Binary mask will be expanded by %.1f voxels plus a soft cosine-edge of %.1f voxels" %
              (expand_width, expand_soft_width))

    if floodfill_rad == None and floodfill_fraction == None:

        # Binarize the low-pass filtered map with one of the thresholds above
        imglpbin = ne.evaluate("imglp > thr")

    else:

        if floodfill_fraction == None:

            if verbose:

                logger.info("Initializing flood-filling method with a sphere of radius %.1f voxels placed at [%d, %d, %d]" % (
                    floodfill_rad, floodfill_xyz[0], floodfill_xyz[1], floodfill_xyz[2]))

            # This will be the initial mask
            inimask = SoftMask(
                imglp.shape, radius=floodfill_rad, width=0, xyz=floodfill_xyz)

        else:

            if verbose:

                logger.info("Initializing flood-filling method binarizing the highest %.1f percent of densities" %
                      (floodfill_fraction * 100))

            floodfill_fraction_thr = np.sort(np.ravel(imglp))[np.round((1.0 - floodfill_fraction) * np.prod(
                imglp.shape)).astype('int')]  # Binarize the voxels with the top floodfill_fraction densities

            # Binarize the low-pass filtered map with one of the thresholds above
            inimask = ne.evaluate("imglp > floodfill_fraction_thr")

        # Binarize the low-pass filtered map using flood-filling approach, works better on non low-pass filtered volumes.
        imglpbin = FloodFilling(imglp, inimask, thr=thr)

    if expand_width > 0:

        # Creates a kernel for expanding the binary mask
        expand_kernel = SoftMask(imglp.shape, radius=expand_width, width=0)

        a = np.fft.rfftn(imglpbin)
        b = np.fft.rfftn(expand_kernel)
        c = np.fft.irfftn(ne.evaluate("a * b"))
        mask_expanded = np.fft.fftshift(ne.evaluate("real(c) > 1e-6"))

    else:

        mask_expanded = imglpbin

    mask_expanded_prev = mask_expanded
    mask_expanded_soft = mask_expanded

    # Expanding with a soft-edge is the same as above but in a loop, 1-voxel-shell at a time, multiplying by a cosine:
    expand_kernel = SoftMask(mask_expanded_prev.shape, radius=1, width=0)
    if expand_soft_width > 0:

        for i in np.arange(1, np.round(expand_soft_width) + 1):
            a = np.fft.rfftn(mask_expanded_prev)
            b = np.fft.rfftn(expand_kernel)
            c = np.fft.irfftn(ne.evaluate("a * b"))
            mask_expanded_new = np.fft.fftshift(
                ne.evaluate("real(c) > 1e-6")).astype('float32')
            mask_expanded_soft = ne.evaluate(
                "mask_expanded_soft + (mask_expanded_new - mask_expanded_prev) * (1.0 + cos(pi * i / (expand_soft_width + 1))) / 2.0")
            mask_expanded_prev = mask_expanded_new

    return mask_expanded_soft


def FloodFilling(img, inimask, thr=0.0):
    # "Smart" growing of binary volume based on flood-filling algorithm.
    # Similar to mask.auto3d processor in EMAN2

    mask = inimask
    expand_kernel = SoftMask(img.shape, radius=1, width=0)

    mask_expanded_prev = mask
    r = 1
    while True:

        mask_expanded_new = np.fft.fftshift(np.fft.irfftn(np.fft.rfftn(
            mask_expanded_prev) * np.fft.rfftn(expand_kernel)).real) > 1e-6  # To prevent residual non-zeros from FFTSs
        shell = mask_expanded_new - mask_expanded_prev
        imgshell = img * shell
        shellbin = imgshell > thr
        if np.any(shellbin):
            mask = mask + shellbin
            mask_expanded_prev = mask
        else:
            break

        r += 1

    return mask


def GetNumberOfFourierSamples(imsize):

    imsize = np.array(imsize)

    return np.round(np.sqrt(np.sum(np.power(imsize, 2))) / 2.0 / np.sqrt(len(imsize))).astype('int') + 1


def GetFreqArray(NSAM=256, apix=1.0):

    return (np.arange(NSAM) / (2.0 * (NSAM - 1) * apix)).reshape(NSAM, 1)


def MaskAutoExpand(map1, map2, apix=1.0, init_lp=15, fraction_threshold=0.01, init_hard_edge=0, init_soft_edge=3, randomize_below_fsc=0.8, fsc_thr=0.143, random_seed=123456789, interp=False, verbose=False):
    # Starts with a tight mask and expands it until masked FSC (roughly) matches the masked-corrected FSC by High-Resolution Noise Substitution

    fsc = {}
    NSAM = GetNumberOfFourierSamples(map1.shape)

    fsc['freq'] = GetFreqArray(NSAM, apix)

    fsc['unmasked'] = FCC(map1, map2)[:NSAM]
    fsc['randomize_below_thr'] = randomize_below_fsc
    fsc['thr'] = fsc_thr

    fsc['rand_res'] = ResolutionAtThreshold(
        fsc['freq'][1:], fsc['unmasked'][1:], randomize_below_fsc, interp=interp)
    rand_freq = 1/fsc['rand_res']
    fsc['unmasked_res'] = ResolutionAtThreshold(
        fsc['freq'][1:], fsc['unmasked'][1:], fsc_thr, interp=interp)

    map1randphase = HighResolutionNoiseSubstitution(
        map1, apix=apix, lp=fsc['rand_res'], random_seed=random_seed)
    map2randphase = HighResolutionNoiseSubstitution(
        map2, apix=apix, lp=fsc['rand_res'], random_seed=random_seed+1)

    mapsum = map1 + map2

    edge = init_hard_edge
    soft_edge = init_soft_edge
    i = 0

    while True:

        automask = AutoMask(mapsum, apix=apix, lp=init_lp, fraction_threshold=fraction_threshold,
                            expand_width=edge, expand_soft_width=soft_edge, verbose=False)

        fsc['masked'] = FCC(map1 * automask, map2 * automask)[:NSAM]
        fsc['masked_res'] = ResolutionAtThreshold(
            fsc['freq'][1:], fsc['masked'][1:], fsc['thr'], interp=interp)

        fsc['masked_randomized'] = FCC(
            map1randphase * automask, map2randphase * automask)[:NSAM]
        fsc['masked_true'] = (
            (fsc['masked'] - fsc['masked_randomized']) / (1.0 - fsc['masked_randomized']))
        fsc['masked_true'][fsc['freq'] <
                           rand_freq] = fsc['masked'][fsc['freq'] < rand_freq]
        fsc['masked_true'] = np.nan_to_num(fsc['masked_true'])
        fsc['masked_true_res'] = ResolutionAtThreshold(
            fsc['freq'][1:], fsc['masked_true'][1:], fsc['thr'], interp=interp)

        if verbose:

            logger.info('Iteration %d, Masked res: %.3f A, True masked res: %.3f A, Current hard edge = %d pix, Current soft edge = %d pix' % (
                i+1, fsc['masked_res'], fsc['masked_true_res'], edge, soft_edge))

        if fsc['masked_true_res'] <= fsc['masked_res']:

            return automask, fsc

        else:

            if i % 2 == 0:

                soft_edge += 1

            else:

                edge += 1

            i += 1


def FilterGauss(img, apix=1.0, lp=-1, hp=-1, return_filter=False):
    # Gaussian band-pass filtering of images.

    rmesh = RadialIndices(img.shape, rounding=False,
                          normalize=True, rfft=True)[0]
    ne.evaluate("rmesh / apix ", out=rmesh)
    rmesh2 = ne.evaluate("rmesh * rmesh")

    if lp <= 0.0:

        lowpass = 1.0

    else:

        lowpass = ne.evaluate("exp(- lp * lp * rmesh2)")

    if hp <= 0.0:

        highpass = 1.0

    else:

        highpass = ne.evaluate("1.0 - exp(- hp * hp * rmesh2)")

    bandpass = ne.evaluate("lowpass * highpass")

    ft = np.fft.rfftn(img)

    filtered = np.fft.irfftn(ne.evaluate("ft * bandpass"), s=img.shape)

    if return_filter:

        return filtered, bandpass

    else:

        return filtered


def FilterWhiten(img, return_filter=False, ps=False):
    # Whitens the spectrum of an image or map, i.e. the radial amplitude spectrum becomes 1.0 at all frequencies.
    # 'ps' is a switch to whiten the Power Spectrum (radial squared amplitudes profile) instead of the amplitude spectrum.
    # Which one to use depends on the application, but the difference in practice is barely noticeable.

    ft = np.fft.fftshift(np.fft.fftn(img))

    if ps:

        a = RotationalAverage(ne.evaluate("real(ft * conj(ft))"))
        radprof = ne.evaluate("sqrt(a)")

    else:

        radprof = RotationalAverage(ne.evaluate("real(abs(ft))"))

    filtered = np.fft.ifftn(np.fft.ifftshift(ne.evaluate("ft / radprof"))).real

    if return_filter:

        return filtered, radprof

    else:

        return filtered


def FilterBfactor(img, apix=1.0, B=0.0, return_filter=False):
    # Applies a B-factor to images. B can be positive or negative.

    rmesh = RadialIndices(img.shape, rounding=False,
                          normalize=True, rfft=True)[0]
    ne.evaluate("rmesh / apix", out=rmesh)
    rmesh2 = ne.evaluate("rmesh * rmesh")

    bfac = ne.evaluate("exp(- (B * rmesh2) / 4)")

    ft = np.fft.rfftn(img)

    filtered = np.fft.irfftn(ne.evaluate("ft * bfac"), s=img.shape)

    if return_filter:

        return filtered, bfac

    else:

        return filtered


def FilterCosine(img, apix=1.0, lp=-1, hp=-1, width=6.0, return_filter=False):
    # Band-pass filtering of images with a cosine edge. Good to approximate a top-hat filter while still reducing edge artifacts.

    if width < 0.0:

        width = 0.0

    if width > 0.0 and width <= 1.0:

        width = 0.5 * width * np.min(img.shape)

    if lp <= 0.0:

        lowpass = 1.0

    else:

        lowpass = SoftMask(img.shape, radius=np.min(
            img.shape) * apix / lp, width=width, rfft=True)

    if hp <= 0.0:

        highpass = 1.0

    else:

        highpass = 1.0 - \
            SoftMask(img.shape, radius=np.min(img.shape)
                     * apix / hp, width=width, rfft=True)

    bandpass = ne.evaluate("lowpass * highpass")

    ft = np.fft.rfftn(img)

    filtered = np.fft.irfftn(ne.evaluate("ft * bandpass"))

    if return_filter:

        return filtered.real, bandpass

    else:

        return filtered.real

def HighResolutionNoiseSubstitution(img, apix=1.0, lp=-1, random_seed=123456789, parallel=False):
    # Randomizes the phases of a map beyond resolution 'lp'
    # If calling many times in parallel, make sure to set the 'parallel' flag to True

    # Get resolution shells:
    rmesh = RadialIndices(img.shape, rounding=False,
                          normalize=True, rfft=True)[0]
    rmesh = ne.evaluate("rmesh / apix", out=rmesh)

    lp = 1.0 / lp

    ft = np.fft.rfftn(img)

    # Decompose Fourier transform into amplitudes and phases:
    amps = ne.evaluate("real(abs(ft))")
    phases = ne.evaluate("arctan2(imag(ft),real(ft))")

    # Select only terms beyond desired resolution (not inclusive)
    idx = ne.evaluate("rmesh > lp")

    if lp > 0.0:

        if parallel:

            # Just to make sure that parallel jobs launched nearly at the same time won't get the same seed (truly random here)
            np.random.seed()

        else:

            np.random.seed(seed=random_seed)

        # Generate random phases in radians
        rndvec = np.random.random(phases.shape)
        phasesrnd = ne.evaluate("rndvec * 2.0 * pi")

        phases[idx] = phasesrnd[idx]

    ftnew = ne.evaluate("amps * (cos(phases) + 1j * sin(phases))")

    return np.fft.irfftn(ftnew, s=img.shape)

def FCC(volume1, volume2, phiArray=[0.0], invertCone=False):
    """
    Fourier conic correlation

    Created on Fri Dec  4 16:35:42 2015
    @author: Robert A. McLeod

    Modified by: Ricardo Righetto
    Date of modification: 23.02.2017
    Change: now also supports (conical) FRC

    Returns FCC_normed, which has len(phiArray) Fourier conic correlations
    """

    if volume1.ndim == 3:

        [M, N, P] = volume1.shape
        [zmesh, ymesh, xmesh] = np.mgrid[-M /
                                         2:M / 2, -N / 2:N / 2, -P / 2:P / 2]
        rhomax = np.int32(
            np.ceil(np.sqrt(M * M / 4.0 + N * N / 4.0 + P * P / 4.0)) + 1)
        rhomesh = ne.evaluate(
            "sqrt(xmesh * xmesh + ymesh * ymesh + zmesh * zmesh)")
        phimesh = ne.evaluate("arccos(zmesh / rhomesh)")
        phimesh[M // 2, N // 2, P // 2] = 0.0
        phimesh = np.ravel(phimesh)

    elif volume1.ndim == 2:

        [M, N] = volume1.shape
        [ymesh, xmesh] = np.mgrid[-M / 2:M / 2, -N / 2:N / 2]
        rhomax = np.int32(np.ceil(np.sqrt(M * M / 4.0 + N * N / 4.0)) + 1)
        rhomesh = ne.evaluate("sqrt(xmesh * xmesh + ymesh * ymesh)")
        phimesh = ne.evaluate("arctan2(ymesh, xmesh)")
        phimesh[M // 2, N // 2] = 0.0
        phimesh = np.ravel(phimesh)

    else:

        raise RuntimeError("Error: FCC only supports 2D and 3D objects.")

    phiArray = ne.evaluate("phiArray * pi / 180.0")

    rhoround = np.round(rhomesh.ravel()).astype('int')  # Indices for bincount

    fft1 = np.ravel(np.fft.fftshift(np.fft.fftn(volume1))).astype('complex128')
    conj_fft2 = np.ravel(np.fft.fftshift(
        np.fft.fftn(volume2)).conj()).astype('complex128')

    FCC_normed = np.zeros([rhomax, len(phiArray)])
    for J, phiAngle in enumerate(phiArray):

        if phiAngle == 0.0:
            fft1_conic = fft1
            conj_fft2_conic = conj_fft2
            rhoround_conic = rhoround
        else:
            conic = np.ravel(ne.evaluate(
                "phimesh <= phiAngle + ((abs(phimesh - pi)) <= phiAngle)"))
            if invertCone:
                conic = np.invert(conic)
            rhoround_conic = rhoround[conic]
            fft1_conic = fft1[conic]
            conj_fft2_conic = conj_fft2[conic]
        FCC = np.bincount(rhoround_conic, ne.evaluate(
            "real(fft1_conic * conj_fft2_conic)"))
        Norm1 = np.bincount(rhoround_conic, ne.evaluate(
            "real(abs(fft1_conic)) * real(abs(fft1_conic))"))
        Norm2 = np.bincount(rhoround_conic, ne.evaluate(
            "real(abs(conj_fft2_conic)) * real(abs(conj_fft2_conic))"))

        goodIndices = np.argwhere(ne.evaluate("(Norm1 * Norm2) > 0.0"))[:-1]
        a = FCC[goodIndices]
        b = Norm1[goodIndices]
        c = Norm2[goodIndices]
        FCC_normed[goodIndices, J] = ne.evaluate("a / sqrt( b * c ) ")

    return FCC_normed

def ResolutionAtThreshold(freq, fsc, thr, interp=True, nyquist_is_fine=False, ):
    # Do a simple linear interpolation (optional) to get resolution value at the specified FSC threshold

    if np.isscalar(thr):

        thr *= np.ones(fsc.shape)

    for i, f in enumerate(fsc):

        if f < thr[i]:

            break

    if i < len(fsc) - 1 and i > 1:

        if interp:

            y1 = fsc[i]
            y0 = fsc[i - 1]
            x1 = freq[i]
            x0 = freq[i - 1]

            delta = (y1 - y0) / (x1 - x0)

            res_freq = x0 + (thr[i - 1] - y0) / delta

        else:

            # Just return the highest resolution bin at which FSC is still higher than threshold:
            res_freq = freq[i - 1]

    elif i == 0:

        res_freq = freq[i]

    else:

        res_freq = freq[-1]

    return 1 / res_freq


def Fsc2Xml(filename, x, y):

    with open(filename, 'w+') as f:
        f.write('<fsc title="" xaxis="Resolution (A-1)" yaxis="Correlation Coefficient">\n')

        for i in np.arange(len(x)):

            f.write('  <coordinate>\n')
            f.write('    <x>%.6f</x>\n' % x[i])
            f.write('    <y>%.6f</y>\n' % y[i])
            f.write('  </coordinate>\n')

        f.write('</fsc>')


def main():

    progname = os.path.basename(sys.argv[0])
    usage = progname + """ <half-map1> [<half-map2>] [options]
	"""

    parser = OptionParser(usage)

    parser.add_option("--out", metavar="postprocess", type="string",
                      default='postprocess', help="Output rootname.")

    parser.add_option("--angpix", metavar=1.0, type="float",
                      help="Pixel size in Angstroems")

    parser.add_option("--fsc_threshold", metavar=0.143, default=0.143, type="float",
                      help="Display the resolution at which the FSC curve crosses this value.")

    parser.add_option("--lowpass", metavar='"auto"', default='auto',
                      help="Resolution (in Angstroems) at which to low-pass filter the final map. A negative value will skip low-pass filtering. Default ('auto') is to low-pass at resolution determined from FSC threshold.")

    parser.add_option("--highpass", metavar='"auto"', default='auto',
                      help="Resolution (in Angstroems) at which to high-pass filter the final map. Useful to to attenuate artefacts such as background ramps (e.g. high-pass at 2/3 of the box size). A negative value will skip high-pass filtering (default).")

    parser.add_option("--mask", metavar="MyMask.mrc", type="string",
                      help="A file containing the mask to be applied to the half-maps before calculating the FSC. Can be combined with other masking options.")

    parser.add_option("--mask_radius", metavar=0.5, default=None, type="float",
                      help="Creates a soft spherical mask. This is the radius of such mask, in pixels or fraction of the box size. Can be combined with other masking options.")

    parser.add_option("--mask_edge_width", metavar=6.0, default=None, type="float",
                      help="This is the width of the cosine edge to soften the outer shells of the spherical mask, in pixels or fraction of the box size.")

    parser.add_option("--automask", action="store_true",
                      help="Do automatic masking of input volumes. Can be combined with other masking options.", default=False)

    parser.add_option("--automask_input", metavar=0, default=0, type="int",
                      help="Which input to provide for auto-masking? 0 = Average of map1 and map2 (default); 1 = Use map1; 2 = Use map2.")

    parser.add_option("--automask_floodfill_radius", metavar=10, default=None, type="float",
                      help="Radius of sphere to initialize flood-filling algorithm in auto-masking, in pixels or fraction of the box size. Typically follows the correct map density for globular-like particles. Use a negative number to disable flood-filling (default).")

    parser.add_option("--automask_floodfill_center", metavar="0,0,0", default=None, type="string",
                      help="Three numbers describing where the center of the sphere should be placed to initialize flood-filling approach in auto-masking (in pixels). Useful to mask parts of the 3D map that are not close to the center. Default is the middle of the box: 0,0,0. Can be positive or negative.")

    parser.add_option("--automask_floodfill_fraction", metavar=0.10, default=None, type="float",
                      help="Use this fraction of the voxels with the highest densities (0.10 = top 10 percent highest densities) to initialize the flood-filling algorithm. Typically follows the correct map density for capsid-like or hollow-center particles. Note that this is only used to initialize the smart masking algorithm and has no influence on the threshold, that is defined independently (see options below).")

    parser.add_option("--automask_lp", metavar=14.0, default=14.0, type="float",
                      help="Resolution (in Angstroems) at which to low-pass filter the input map for auto-masking purposes. Should typically be in the range of 10-20 A. However if using the flood-filling approach a value in the range 5-10 A might work better. Use a negative number to disable this filter.")

    parser.add_option("--automask_lp_edge_width", metavar=5.0, default=5.0, type="float",
                      help="Width of the cosine-edge low-pass filter to be used for auto-masking (in Fourier pixels).")

    parser.add_option("--automask_lp_gauss", action="store_true", default=False,
                      help="Use a Gaussian instead of cosine-edge low-pass filter for auto-masking.")

    parser.add_option("--automask_threshold", metavar=0.02, default=None, type="float",
                      help="Absolute threshold to generate the initial binary volume in auto-masking. This has precedence over --automask_fraction and --automask_sigma.")

    parser.add_option("--automask_fraction", metavar=0.10, default=None, type="float",
                      help="Use this fraction of the voxels with the highest densities (0.10 = top 10 percent highest densities) to generate the initial binary volume in auto-masking. This has precedence over --automask_sigma.")

    parser.add_option("--automask_sigma", metavar=1.0, default=1.0, type="float",
                      help="Use this many standard deviations above the mean density value as threshold for initial binary volume generation in auto-masking. This is the default option.")

    parser.add_option("--automask_expand_width", metavar=3.0, default=3.0, type="float",
                      help="Width in pixels to expand the binary mask in auto-masking. Useful to make the mask more generous and correct for imperfections of the initial binarization.")

    parser.add_option("--automask_soft_width", metavar=6.0, default=6.0, type="float",
                      help="Width in pixels to expand the binary mask in auto-masking with a soft cosine edge. Very important to prevent artificial correlations induced by the mask.")

    parser.add_option("--automask_optimize", action="store_true",
                      help="Will generate a mask automatically based on the automask procedure, and then tune it to optimize the masked FSC corrected by High-Resolution Noise Substitution (Chen et al, Ultramicroscopy 2013)", default=False)

    parser.add_option("--skip_fsc", action="store_true",
                      help="Skip all FSC calculations, only do masking and filtering stuff.", default=False)

    parser.add_option("--mw", metavar=1000.0, type="float", help="Molecular mass in kDa of particle or helical segment comprised within the mask. Needed to calculate volume-normalized Single-Particle Wiener filter (Sindelar & Grigorieff, JSB 2012). If not specified, will do conventional FSC weighting on the final map (Rosenthal & Henderson, JMB 2003).")

    parser.add_option("--mw_ignore", metavar=0.0, type="float", default=0.0, help="CAUTION! EXPERIMENTAL OPTION: Molecular mass in kDa present within the mask that needs to be ignored. Needed to calculate an adaptation of the volume-normalized Single-Particle Wiener filter (Sindelar & Grigorieff, JSB 2012). Only used if --mw is also specified. May be useful if your particles are extracted from 2D crystals.")

    parser.add_option("--skip_fsc_weighting", action="store_true",
                      help="Do NOT apply FSC weighting (Rosenthal & Henderson, JMB 2003) to the final map, nor the Single-Particle Wiener filter (Sindelar & Grigorieff, JSB 2012).", default=False)

    parser.add_option("--gaussian", action="store_true",
                      help="Apply a Gaussian (instead of cosine-edge) low-pass filter to the map, with cutoffs defined by --highpass and --lowpass.", default=False)

    parser.add_option("--cosine", action="store_true", help="Apply a cosine-edge low-pass filter to the final map, with cutoffs defined by --highpass and --lowpass. This is the default. The width of the cosine edge can be specified with the option --edge_width.", default=True)

    parser.add_option("--cosine_edge_width", metavar=3.0, type="float",
                      help="Width of the cosine-edge filter (in Fourier pixels). The cutoff frequency will have a weight of 0.5, with corresponding weighting above and below following the cosine falloff. If set to zero, becomes a top-hat filter with weighting of 1.0 at the cutoff frequency.", default=3.0)

    parser.add_option("--tophat", action="store_true",
                      help="Apply a top-hat low-pass filter to the final map. Equivalent to specifying --cosine with --cosine_edge_width=0.", default=False)

    parser.add_option("--mtf", type="string",
                      help="File containing the detector MTF for sharpening of the final map.")

    parser.add_option("--auto_bfac", metavar="10.0,0.0", default=None, type="string", help="Estimate B-factor automatically using information in this resolution range, in Angstroems (lowres,highres). This works based on the Guinier plot, which should ideally be a straight line from ~10.0 A and beyond (Rosenthal & Henderson, JMB 2003).'If you set lowres and/or maxres to -1, these values will be calculated automatically. MTF and FSC weighting information are employed, if not ommitted.")

    parser.add_option("--adhoc_bfac", metavar=0.0, type="float",
                      help="Apply an ad-hoc B-factor to the map (in Angstroems^2). Can be positive (smoothing) or negative (sharpening).", default=0.0)

    parser.add_option("--whiten", action="store_true", help="Whiten the final map (that is, makes the radial Amplitude Spectrum equal to 1.0 across all frequencies). Should normally be used in combination with the option --gaussian and --skip_fsc_weighting, and also --highpass in some cases. If using this option, B-factor and MTF sharpening become meaningless.", default=False)

    parser.add_option("--whiten_amps", action="store_true", help="Whiten the radial Amplitude Spectrum instead of the radial Power Spectrum (Amplitudes^2). Whitening amplitudes seems to give a slightly more peaky (sharp) map as measured by kurtosis, but the results are visually almost identical. Only valid if using option --whiten above.", default=False)

    parser.add_option("--randomize_below_fsc", metavar=0.8, type="float", default=None,
                      help="If provided, will randomize phases for all Fourier shells beyond the point where the FSC drops below this value, to assess correlations introduced by the mask by High-Resolution Noise Substitution (Chen et al, Ultramicroscopy 2013). Be aware that this procedure may introduce a 'dip' in the FSC curves at the corresponding resolution value, but that is normal.")

    parser.add_option("--randomize_beyond", metavar=10, type="float", default=None,
                      help="If provided, will randomize phases for all Fourier shells beyond this resolution shell, to assess correlations introduced by the mask by High-Resolution Noise Substitution (Chen et al, Ultramicroscopy 2013). Be aware that this procedure may introduce a 'dip' in the FSC curves at the corresponding resolution value, but that is normal.")

    parser.add_option("--random_seed", metavar=123456789, type="int", default=123456789,
                      help="Choose the random seed for High-Resolution Noise Substitution (see option --randomize_below_fsc above)")

    parser.add_option("--flip_x", action="store_true", default=False,
                      help="Invert handedness of input volumes along the X axis.")

    parser.add_option("--flip_y", action="store_true", default=False,
                      help="Invert handedness of input volumes along the Y axis.")

    parser.add_option("--flip_z", action="store_true", default=False,
                      help="Invert handedness of input volumes along the Z axis.")

    parser.add_option("--xml", action="store_true", default=False,
                      help="Save FSC curves also in XML format for EMDB deposition.")

    (options, args) = parser.parse_args()

    command = ' '.join(sys.argv)

    if options.lowpass != 'auto':

        options.lowpass = float(options.lowpass)

    if options.highpass != 'auto':

        options.highpass = float(options.highpass)

    if options.mw != None and options.mw < 0.0:

        logger.error('Molecular mass cannot be negative!')
        sys.exit(1)

    if options.mw_ignore != None and options.mw_ignore < 0.0:

        logger.error('Molecular mass to be ignored cannot be negative!')
        sys.exit(1)

    if options.angpix == None:

        logger.warning('Pixel size was not specified. Assuming 1.0 A/pixel.')
        options.angpix = 1.0

    elif options.angpix <= 0.0:

        logger.error('Pixel size must be greater than zero!')
        sys.exit(1)

    if options.cosine_edge_width != None and options.cosine_edge_width < 0.0:

        logger.error('Cosine edge width cannot be negative!')
        sys.exit(1)

    if options.randomize_below_fsc != None and (options.randomize_below_fsc < -1.0 or options.randomize_below_fsc > 1.0):

        logger.error(
            'FSC values for phase-randomization must be in the range [-1,1]!')
        sys.exit(1)

    if options.tophat:

        options.gaussian = False
        options.cosine = True
        options.cosine_edge_width = 0.0

    mask_center = [0, 0, 0]

    if options.automask_floodfill_center == None:

        options.automask_floodfill_center = [0, 0, 0]

    else:

        options.automask_floodfill_center = np.array(
            map(int, options.automask_floodfill_center.split(',')))

    if options.skip_fsc and options.lowpass == "auto":

        options.lowpass = -1
        options.skip_fsc_weighting = True

    fsc_interp = False

    # Read in the two maps:
    map1 = mrc.read(args[0])
    common_header = mrc.readHeaderFromFile(args[0])

    if len(args) > 1:
        map2 = mrc.read(args[1])
    else:
        map2 = map1
    sys.stdout = sys.__stdout__

    if options.flip_x:

        logger.info('Flipping input maps along X')

        map1 = map1[:, :, ::-1]
        map2 = map2[:, :, ::-1]

    if options.flip_y:

        logger.info('Flipping input maps along Y')

        map1 = map1[:, ::-1, :]
        map2 = map2[:, ::-1, :]

    if options.flip_z:

        logger.info('Flipping input maps along Z')

        map1 = map1[::-1, :, :]
        map2 = map2[::-1, :, :]

    if np.any(map1.shape != map2.shape):

        logger.error('Input maps must be the same size!')
        sys.exit(1)

    # We check if there is a mask file and if not, should we create one?
    if options.mask != None:

        sys.stdout = open(os.devnull, "w")  # Suppress output
        maskfile = mrc.read(options.mask)
        sys.stdout = sys.__stdout__

    else:

        maskfile = np.ones( map1.shape )

    mask = maskfile

    if options.mask_radius != None or options.mask_edge_width != None:

        if options.mask_radius == None:

            options.mask_radius = 0.5

        if options.mask_edge_width == None:

            options.mask_edge_width = 6.0

        masksphere = SoftMask(
            map1.shape, radius=options.mask_radius, width=options.mask_edge_width, xyz=mask_center)

        ne.evaluate( "mask * masksphere", out=mask)

    if options.automask:

        if options.automask_input == 0:

            maskautoin = ne.evaluate( "0.5 * (map1 + map2)" )

        elif options.automask_input == 1:

            maskautoin = map1

        elif options.automask_input == 2:

            maskautoin = map2

        maskauto = AutoMask(maskautoin, apix=options.angpix, lp=options.automask_lp, gaussian=options.automask_lp_gauss, cosine_edge_width=options.automask_lp_edge_width, absolute_threshold=options.automask_threshold, fraction_threshold=options.automask_fraction, sigma_threshold=options.automask_sigma,
                                 expand_width=options.automask_expand_width, expand_soft_width=options.automask_soft_width, floodfill_rad=options.automask_floodfill_radius, floodfill_xyz=options.automask_floodfill_center, floodfill_fraction=options.automask_floodfill_fraction, verbose=True)

        ne.evaluate( "mask * maskauto ", out=mask)

    if options.automask_optimize:

        logger.info('Starting mask optimization')
        mask,fsc_optimized = MaskAutoExpand(map1, map2, apix=options.angpix, init_lp=options.automask_lp, fraction_threshold=0.01, init_hard_edge=0, init_soft_edge=3, randomize_below_fsc=0.8, fsc_thr=options.fsc_threshold, random_seed=options.random_seed, interp=False, verbose=True)
        logger.info('Done optimizing mask.')

    # If a spherical mask or an auto-mask were created, we need to save it (this will be the combination of all masks provided or created!):
    if options.mask_radius or options.automask or options.automask_optimize:

        mrc.write(mask, options.out + '-mask.mrc', header=common_header)

        options.mask = options.out + '-mask.mrc'

    # Resolution range to estimate B-factor:
    if options.auto_bfac != None:

        resrange = options.auto_bfac.split(',')
        minres = float(resrange[0])
        maxres = float(resrange[1])

    # For cubic volumes this is just half the box size + 1.
    NSAM = GetNumberOfFourierSamples( map1.shape )

    freq = GetFreqArray( NSAM, options.angpix )

    freq[0] = 1.0 / 999  # Just to avoid dividing by zero later
    freq2 = ne.evaluate( "freq * freq" )

    # Start creating the matrix that will be written to an output file
    dat = np.append(1.0 / freq, freq, axis=1)
    # Header of the output file describing the data columns
    head = 'Res       \t1/Res     \t'

    if not options.skip_fsc:

        # logger.info('Calculating unmasked FSC')

        fsc = FCC(map1, map2)

        res = ResolutionAtThreshold(
            freq[1:], fsc[1:NSAM], options.fsc_threshold, fsc_interp)
        # logger.info('FSC >= %.3f until %.3f A (unmasked)' %
        #        (options.fsc_threshold, res))

        # logger.info('Area under FSC (unmasked): %.3f' % fsc[1:NSAM].sum())

        dat = np.append(dat, fsc[:NSAM], axis=1)  # Append the unmasked FSC
        head += 'FSC-unmasked\t'
        if options.xml:
          Fsc2Xml( options.out+'_fsc-unmasked.xml', freq, fsc[:NSAM] )


        # Now we go to the mask-related operations which are activated if a mask or MW are specified. If only
        if options.mask != None or options.mw != None:

            if options.mask == None:  # If MW is specified but no mask, we issue a warning:

                logger.warning('You specified MW without a mask. This may produce inaccurate results!')

                mask = np.ones(map1.shape, dtype='float')
                mrc.write(mask, options.out + '-mask.mrc', header=common_header)
                options.mask = options.out + '-mask.mrc'

            map1masked = ne.evaluate( "map1 * mask" )
            map2masked = ne.evaluate( "map2 * mask" )

            # logger.info('Calculating masked FSC')

            fsc_mask = FCC(map1masked, map2masked)

            res_mask = ResolutionAtThreshold(
                freq[1:], fsc_mask[1:NSAM], options.fsc_threshold, fsc_interp)
            # logger.info('FSC >= %.3f until %.3f A (masked)' %
            #        (options.fsc_threshold, res_mask))

            # logger.info('Area under FSC (masked): %.3f' % fsc_mask[1:NSAM].sum())

            # Append the masked FSC
            dat = np.append(dat, fsc_mask[:NSAM], axis=1)
            head += 'FSC-masked\t'
            if options.xml:
              Fsc2Xml( options.out+'_fsc-masked.xml', freq, fsc_mask[:NSAM] )

            if options.randomize_below_fsc == None and options.randomize_beyond == None:
                pass
            else:

                if options.randomize_beyond == None:

                  rand_res = ResolutionAtThreshold(
                      freq[1:], fsc[1:NSAM], options.randomize_below_fsc, fsc_interp)

                else:

                  rand_res = options.randomize_beyond

                logger.info('Randomizing phases beyond %.3f A' % rand_res)
                rand_freq = 1.0 / rand_res

                # We have to enforce the random seed otherwise different runs would not be comparable
                map1randphase = HighResolutionNoiseSubstitution(
                    map1, apix=options.angpix, lp=rand_res, random_seed=options.random_seed )

                # Cannot use same random seed for both maps!!!
                map2randphase = HighResolutionNoiseSubstitution(
                    map2, apix=options.angpix, lp=rand_res, random_seed=options.random_seed + 1 )

                # We mask the phase-randomized maps:
                map1randphasemasked = ne.evaluate( "map1randphase * mask" )
                map2randphasemasked = ne.evaluate( "map2randphase * mask" )

                # logger.info('Calculating masked FSC for phase-randomized maps')

                fsc_mask_rnd = FCC(
                    map1randphasemasked, map2randphasemasked)

                dat = np.append(dat, fsc_mask_rnd[:NSAM], axis=1)
                head += 'FSC-phase-randomized\t'
                # We compute FSCtrue following (Chen et al, Ultramicroscopy 2013). For masked maps this will correct the FSC for eventual refinement overfitting, including from the mask:

                # fsc_mask_true[freq >= rand_freq] = (fsc_mask[freq >= rand_freq] - fsc_mask_rnd[freq >= rand_freq]) / (1 - fsc_mask_rnd[freq >= rand_freq])
                rand_freq_2step = 1.0 / (rand_res - 2)
                fsc_mask_true = ((fsc_mask - fsc_mask_rnd) / (1.0 - fsc_mask_rnd))
                fsc_mask_true[:NSAM][freq < rand_freq_2step] = fsc_mask[:NSAM][freq < rand_freq_2step]
                fsc_mask_true = np.nan_to_num(fsc_mask_true)

                res_mask_true = ResolutionAtThreshold(
                    freq[1:], fsc_mask_true[1:NSAM], options.fsc_threshold, fsc_interp)
                # logger.info('FSC >= %.3f until %.3f A (masked - true)' %
                #        (options.fsc_threshold, res_mask_true))

                # logger.info('Area under FSC (masked - true): %.3f' % fsc_mask_true[1:NSAM].sum())

                # Append the true masked FSC
                dat = np.append(dat, fsc_mask_true[:NSAM], axis=1)
                head += 'FSC-masked_true\t'
                if options.xml:
                  Fsc2Xml( options.out+'_fsc-masked_true.xml', freq, fsc_mask_true[:NSAM] )

                res_mask = res_mask_true

            if options.mw != None:

                DALT = 0.81  # Da/A^3

                # Estimate fraction of volume occupied by the molecule:
                fpart = 1000.0 * options.mw / DALT / \
                    (options.angpix * 2 * NSAM)**3

                fignore = 1000.0 * options.mw_ignore / \
                    DALT / (options.angpix * 2 * NSAM)**3

                # Fraction of the volume occupied by the mask:
                maskvoxsum = ne.evaluate( "sum(mask * mask)" )
                fmask = maskvoxsum / np.prod(mask.shape)

                logger.info('Calculating Single-Particle Wiener filter')
                logger.info('Fraction of particle within the volume (Fpart): %.6f' % fpart)
                logger.info('Fraction of mask within the volume (Fmask): %.6f' % fmask)
                if options.mw_ignore > 0.0:

                    logger.info(
                        'Fraction of densities to be ignored within the volume (Fignore): %.6f' % fignore)
                    logger.info('Fpart/(Fmask-Fignore) ratio: %.6f' %
                          (fpart / (fmask - fignore)))

                    if (fpart / (fmask - fignore)) >= 1.0:

                        logger.warning('Your particle occupies a volume bigger than the mask. Mask is probably too tight or even too small!')

                else:

                    logger.info('Fpart/Fmask ratio: %.6f' % (fpart / fmask))

                    if (fpart / fmask) >= 1.0:

                        logger.warning('Your particle occupies a volume bigger than the mask. Mask is probably too tight or even too small!')

                # Let's do Single-Particle Wiener filtering following (Sindelar & Grigorieff, 2012):

                if options.randomize_below_fsc == None:

                    fsc_spw = fsc_mask / \
                        (fsc_mask + (fpart / (fmask - fignore)) * (1.0 - fsc_mask))

                else:

                    fsc_spw = fsc_mask_true / \
                        (fsc_mask_true + (fpart / (fmask - fignore))
                         * (1.0 - fsc_mask_true))

                res_spw = ResolutionAtThreshold(
                    freq[1:], fsc_spw[1:NSAM], options.fsc_threshold, fsc_interp)
                # logger.info('FSC >= %.3f until %.3f A (volume-normalized)' %
                #        (options.fsc_threshold, res_spw))

                # logger.info('Area under FSC (volume-normalized): %.3f' % fsc_spw[1:NSAM].sum())

                # Append the FSC-SPW
                dat = np.append(dat, fsc_spw[:NSAM], axis=1)
                head += 'FSC-SPW   \t'
                if options.xml:
                  Fsc2Xml( options.out+'_fsc-spw.xml', freq, fsc_spw[:NSAM] )

    else:

        logger.info('Skipping FSC calculations')

    # 1. Sum the two half-reconstructions:
    fullmap = ne.evaluate( "0.5 * (map1 + map2)" )

    radamp_original = RadialProfile( fullmap, amps=True )[:NSAM]
    lnF_original = np.log(radamp_original)

    # 2. Apply FSC weighting or SPW filter to the final map, accordingly:
    if options.skip_fsc_weighting == False:

        logger.info('Applying FSC weighting')
        if options.mask == None and options.mw == None:

            # Derive weights from unmasked FSC
            fsc_weights = np.zeros(fsc.shape)
            idx = fsc > 0.0
            fsc_weights[idx] = np.sqrt(2 * fsc[idx] / (1 + fsc[idx]))

        elif options.mw == None:

            # Derive weights from masked FSC
            if options.randomize_below_fsc != None:

                fsc_weights = np.zeros(fsc_mask_true.shape)
                idx = fsc_mask_true > 0.0
                fsc_weights[idx] = np.sqrt(
                    2 * fsc_mask_true[idx] / (1 + fsc_mask_true[idx]))

            else:

                fsc_weights = np.zeros(fsc_mask.shape)
                idx = fsc_mask > 0.0
                fsc_weights[idx] = np.sqrt(
                    2 * fsc_mask[idx] / (1 + fsc_mask[idx]))

        else:

            fsc_weights = np.zeros(fsc_spw.shape)
            idx = fsc_spw > 0.0
            fsc_weights[idx] = np.sqrt(2 * fsc_spw[idx] / (1 + fsc_spw[idx]))

        if options.mw != None:

          rmax = res_spw

        elif options.mask != None:

          rmax = res_mask

        else:

          rmax = res

        fullmap = RadialFilter(fullmap, fsc_weights, return_filter=False)

        # Append the FSC weighting
        dat = np.append(dat, fsc_weights[:NSAM], axis=1)
        head += 'Cref_Weights\t'

    # 3. Sharpen map by recovering amplitudes from detector's MTF:
    if options.mtf != None:

        logger.info('Dividing map by the detector MTF')

        try:

            mtf = np.loadtxt(options.mtf)

            ignore_mtf = False

        except ValueError:

            if options.mtf[-5:] == '.star':

                mtf = np.loadtxt(options.mtf, skiprows=4)

                ignore_mtf = False

            else:

                logger.warning('Could not read MTF file! Ignoring MTF')
                ignore_mtf = True

        if ignore_mtf == False:

            # We need to know the MTF values at the Fourier bins of our map. So we interpolate from the MTF description available:

            # For cubic volumes this is just half the box size multiplied by sqrt(2).
            NSAMfull = np.ceil(
                np.sqrt(np.sum(np.power(map1.shape, 2))) / 2.0 + 1).astype('int')
            freqfull = (np.arange(NSAMfull) / (2.0 * NSAM *
                                               options.angpix)).reshape(NSAMfull, 1)
            freqfull[0] = 1.0 / 999  # Just to avoid dividing by zero later

            interp_mtf = np.interp(
                freqfull, mtf[:, 0] / options.angpix, mtf[:, 1])

            # Divide Fourier components by the detector MTF:
            inv_mtf = 1.0 / interp_mtf

            fullmap = RadialFilter(fullmap, inv_mtf, return_filter=False)

            # Append the inverse MTF applied
            dat = np.append(dat, inv_mtf[:NSAM], axis=1)
            head += 'InverseMTF\t'

    # 4. Perform automatic sharpening based on the Guinier plot:

    ##### GUINIER PLOT #####
    if options.auto_bfac != None:

        # Here we use the same method as relion_postprocess. Note there is a difference in the normalization of the FFT, but that doesn't affect the results (only the intercept of fit).
        # NOTE: the bfactor.exe and EM-BFACTOR programs use a different fitting method.
        radamp = RadialProfile( fullmap, amps=True )[:NSAM] # We use the unmasked map to avoid overestimating the sharpening B-factor
        lnF = np.log(radamp)
        if minres <= 0:
            minres = 10.0
        if maxres <= 0:

            if not options.skip_fsc:

                if options.mw != None:

                    maxres = res_spw

                elif options.mask != None:

                    if options.randomize_below_fsc != None:

                        maxres = res_mask_true

                    else:

                        maxres = res_mask

                else:

                    maxres = res

            else:

              maxres = 2 * options.angpix

        logger.info('Estimating contrast decay (B-factor) from Guinier plot between %.3f A and %.3f A' % (minres, maxres))

        hirange = 1. / freq <= minres
        lorange = 1. / freq >= maxres
        resrange = hirange * lorange
        resrange = resrange[:, 0]
        fit = np.polyfit(freq2[resrange, 0], lnF[resrange], deg=1)
        fitline = fit[0] * freq2 + fit[1]
        logger.info('Slope of fit: %.4f' % (fit[0]))
        logger.info('Intercept of fit: %.4f' % (fit[1]))
        logger.info('Correlation of fit: %.5f' %
              (np.corrcoef(lnF[resrange], fitline[resrange, 0])[0, 1]))
        logger.info('B-factor for contrast restoration: %.4f A^2' % (4.0 * fit[0]))

        fullmap = FilterBfactor(
            fullmap, apix=options.angpix, B=4.0 * fit[0], return_filter=False)
        # Just for appending to the output data file
        guinierfilt = np.exp(- fit[0] * freq2)
        # Append the B-factor filter derived from the Guinier plot
        dat = np.append(dat, guinierfilt[:NSAM], axis=1)
        head += 'Auto_B-factor\t'

        radampnew = RadialProfile(fullmap, amps=True)[:NSAM]
        lnFnew = np.log(radampnew)

        if options.cosine == False:

            logger.warning('You should probably specify --cosine or --tophat option to band-pass filter your map after sharpening!')

    # 5. Apply an ad-hoc B-factor for smoothing or sharpening the map, if provided:
    if options.adhoc_bfac != 0.0:
        logger.info('Applying ad-hoc B-factor to the map')

        fullmap = FilterBfactor(
            fullmap, apix=options.angpix, B=options.adhoc_bfac, return_filter=False)
        freq2 = freq * freq
        # Just for appending to the output data file
        bfacfilt = np.exp(- options.adhoc_bfac * freq2 / 4.0)

        # Append the ad-hoc B-factor filter applied
        dat = np.append(dat, bfacfilt[:NSAM], axis=1)
        head += 'Adhoc_B-factor\t'

        if options.cosine == False:

            logger.warning('You should probably specify --cosine or --tophat option to band-pass filter your map after sharpening!')

    if options.whiten:

        logger.info('Whitening the map')
        # Below, use ps=True to whiten the radial Power Spectrum (cisTEM) instead of the Amplitude Spectrum (IMAGIC). Results are visually almost identical, but whitening amplitudes seems to give a slightly more "peaky" (sharp) map as measured by kurtosis.
        whitened, filt = FilterWhiten(
            ne.evaluate( "fullmap * mask" ), ps=~options.whiten_amps, return_filter=True)
        fullmap = RadialFilter(fullmap, 1. / RadialProfile(filt))

    # 7. Impose a Gaussian or Cosine or Top-hat low-pass filter with cutoff at given resolution, or resolution determined from FSC threshold:
    if options.lowpass == 'auto' or options.lowpass >= 0.0 or options.highpass >= 0.0:

        if options.lowpass == 'auto':

            if options.mw != None:

                options.lowpass = res_spw

            elif options.mask != None:

                options.lowpass = res_mask

            else:

                options.lowpass = res

        # if options.highpass == 'auto':

        # 	options.highpass = 2.0 * ( NSAM - 1 ) * options.angpix / 3

        if options.highpass == 'auto':

            hipass_print = 2.0 * (NSAM - 1) * options.angpix
            options.highpass = -1

        else:

            hipass_print = options.highpass

        if options.lowpass <= 0.0:

            lopass_print = 2 * options.angpix

        else:

            lopass_print = options.lowpass

        logger.info('Band-pass filtering between resolution cutoffs %.3f A and %.3f A' %
              (hipass_print, lopass_print))

        if options.gaussian:

            fullmap = FilterGauss(
                fullmap, apix=options.angpix, lp=options.lowpass, hp=options.highpass, return_filter=False)
            if options.lowpass <= 0.0:

                lp = np.ones(freq2[:, 0].shape)

            else:

                lp = np.exp(- options.lowpass ** 2 * freq2[:, 0])

            if options.highpass <= 0.0:

                hp = np.ones(freq2[:, 0].shape)

            else:

                hp = 1.0 - np.exp(- options.highpass ** 2 * freq2[:, 0])

            bp = hp * lp

        else:

            fullmap = FilterCosine(fullmap, apix=options.angpix, lp=options.lowpass,
                                        hp=options.highpass, return_filter=False, width=options.cosine_edge_width)

            if options.lowpass <= 0.0:

                lp = np.ones(freq2[:, 0].shape)

            else:

                cosrad = np.argmin(np.abs(1. / freq - options.lowpass))
                rii = cosrad + options.cosine_edge_width / 2
                rih = cosrad - options.cosine_edge_width / 2
                lp = np.zeros(freq[:, 0].shape)
                r = np.arange(len(freq))
                fill_idx = r <= rih
                lp[fill_idx] = 1.0
                rih_idx = r > rih
                rii_idx = r <= rii
                edge_idx = rih_idx * rii_idx
                lp[edge_idx] = (
                    1.0 + np.cos(np.pi * (r[edge_idx] - rih) / options.cosine_edge_width)) / 2.0

            if options.highpass <= 0.0:

                hp = np.ones(freq2[:, 0].shape)

            else:

                # The 1e-8 is just to ensure that the specified frequency is INCLUDED in the filter (not cancelled)
                cosrad = np.argmin(np.abs(1. / freq - options.highpass))
                rii = cosrad + options.cosine_edge_width / 2
                rih = cosrad - options.cosine_edge_width / 2
                hp = np.zeros(freq[:, 0].shape)
                r = np.arange(len(freq))
                fill_idx = r <= rih
                hp[fill_idx] = 1.0
                rih_idx = r > rih
                rii_idx = r <= rii
                edge_idx = rih_idx * rii_idx
                hp[edge_idx] = (
                    1.0 + np.cos(np.pi * (r[edge_idx] - rih) / options.cosine_edge_width)) / 2.0
                hp = 1.0 - hp

            bp = hp * lp

        # Append the band-pass filter applied
        dat = np.append(dat, bp.reshape(NSAM, 1), axis=1)
        head += 'Band-pass  \t'

    # 8. Apply mask, if provided:
    if options.mask != None or options.mw != None:
        # logger.info('Masking the map')
        masked = ne.evaluate( "fullmap * mask" )

        mrc.write(masked, options.out + '-masked.mrc', header=common_header)

    # Write filtered, unmasked map
    mrc.write(fullmap, options.out + '-unmasked.mrc', header=common_header)

    if not options.skip_fsc:

        # Save output file with all relevant FSC data
        np.savetxt(options.out + '_data.fsc', np.matrix(dat),
                   header=command + '\n' + head, delimiter='\t', fmt='%.6f')

if __name__ == "__main__":
    main()
