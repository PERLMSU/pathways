"""
This module contains functions that parse raw data columns into 
better columns. The module when run as a script should parse raw
data files into new columns:

physics major at one time - binary
semester index - integer
major category - string
z-score - float
"""

def convert_term_code(term_code):
    """
    converts msu termcodes from string format to decimal format

    this function does not support the older quarter system
    designations.

    termcode : str
    year : int
    semester_index : int
    """

    # semester codes are as follows:
    # SS : Spring Semester
    # US : Summer Semester
    # FS : Fall Semester
    semester_codes = {'SS':1, 'US':2, 'FS':3}
    
    semester = term_code[0:2]
    year = int(term_code[2:4]) + 2000

    semester_index = semester_codes[semester]
    
    return year, semester_index

def current_term_index(current_term, first_term):
    """
    returns the number of terms since student first enrolled.

    current_term : tuple
    first_term : tuple
    ft_year : int
    ft_semester : int
    ct_year = int
    ct_semester = int
    year_diff = int
    semester_diff = int
    """
    ft_year = first_term[0]
    ft_semester = first_term[1]
    ct_year = current_term[0]
    ct_semester = current_term[1]
    
    # years are made up of essentially 3 semester units
    # thus we need to convert year units into semester
    # units so we can combine them
    year_diff =  3*(ct_year - ft_year)
    semester_diff = ct_semester - ft_semester
    return year_diff + semester_diff

def calc_z_score(data_array):
    """
    calculates z score of an array of floats

    this might be a pd.Series instead. maybe

    data_array : np.ndarray
    return : np.ndarray
    """
    avg = data_array.mean()
    std = data_array.std()
    return (data_array - avg)/std

def convert_major_to_major_category(major):
    """
    converts major (e.g., physics, history, etc) to
    major category (e.g., physics, non-stem) based on
    look up table.

    The lookup table is assumed to be complete. It was created
    from previous work by an undergraduate that identified all
    majors.

    major : str
    return : str
    """
    major_category_lookup = {'Accounting': 'Other STEM',
    'Actuarial Science': 'Other STEM',
    'Advertising': 'Non STEM',
    'African American & African Std': 'Non STEM',
    'Ag,Food & Natural Resources Ed': 'Other STEM',
    'Agr & Nat Res   No Preference': 'Other STEM',
    'Agri Business': 'Other STEM',
    'Agribusiness Management': 'Other STEM',
    'Agric & Natural Resources Comm': 'Other STEM',
    'Agricultural Engineering': 'Engineering',
    'Agricultural Engineering Tech': 'Engineering',
    'Agricultural Industries': 'Other STEM',
    'Agricultural Operations': 'Other STEM',
    'Agriscience': 'Other STEM',
    'American Studies': 'Non STEM',
    'Ancient Studies': 'Non STEM',
    'Animal Husbandry': 'Other STEM',
    'Animal Science': 'Other STEM',
    'Anthropology': 'Other STEM',
    'Apparel Design and Textiles': 'Non STEM',
    'Apparel and Textile Design': 'Non STEM',
    'Apparel and Textiles': 'Non STEM',
    'Applied Engineering Sciences': 'Engineering',
    'Applied Mathematics': 'Other STEM',
    'Applied Music': 'Non STEM',
    'Applied Plant Science': 'Other STEM',
    'Applied Statistics': 'Other STEM',
    'Arabic': 'Non STEM',
    'Art Education': 'Education',
    'Art History and Visual Culture': 'Non STEM',
    'Art Practice': 'Non STEM',
    'Arts & Letters   General': 'Non STEM',
    'Arts and Humanities': 'Non STEM',
    'Astrophysics': 'Physics',
    'Astrophysics and Astronomy': 'Physics',
    'Athletic Training': 'Non STEM',
    'Audiology and Speech Sciences': 'Other STEM',
    'Beef Cattle Management': 'Other STEM',
    'Biochem&Molecular Biol/Biotech': 'Other STEM',
    'Biochemistry': 'Other STEM',
    'Biochemistry & Molecular Biol': 'Other STEM',
    'Biochemistry/Biotechnology': 'Other STEM',
    'Biological Science': 'Other STEM',
    'Biological Science Interdept': 'Other STEM',
    'Biology': 'Other STEM',
    'Biomedical Laboratory Science': 'Other STEM',
    'Biosystems Engineering': 'Engineering',
    'Botany': 'Other STEM',
    'Botany and Plant Pathology': 'Other STEM',
    'Building Construction Mgt': 'Other STEM',
    'Business Administration': 'Non STEM',
    'Business Admitted': 'Non STEM',
    'Business Analytics': 'Non STEM',
    'Business Preference': 'Non STEM',
    'Cell and Molecular Biology': 'Other STEM',
    'Chemical Engineering': 'Engineering',
    'Chemical Physics': 'Other STEM',
    'Chemistry': 'Other STEM',
    'Child Development': 'Non STEM',
    'Chinese': 'Non STEM',
    'Civil Engineering': 'Engineering',
    'Classical Studies': 'Non STEM',
    'Clinical Laboratory Sciences': 'Other STEM',
    'Clinical Social Work': 'Non STEM',
    'Commercial Floriculture': 'Non STEM',
    'Communication': 'Other STEM',
    'Communicative Sci & Disorders': 'Other STEM',
    'Community Sustainability': 'Non STEM',
    'Comparative Culture & Politics': 'Non STEM',
    'Composition': 'Non STEM',
    'Composition and Music Theory': 'Non STEM',
    'Computational Chemistry': 'Other STEM',
    'Computational Mathematics': 'Other STEM',
    'Computer Engineering': 'Engineering',
    'Computer Science': 'Other STEM',
    'Construction Management': 'Non STEM',
    'Criminal Justice': 'Non STEM',
    'Criminalistics': 'Non STEM',
    'Crop and Soil Sciences': 'Other STEM',
    'Curriculum and Teaching': 'Education',
    'Dairy Management': 'Non STEM',
    'Dairy Production': 'Non STEM',
    'Diagnostic Molecular Science': 'Other STEM',
    'Dietetics': 'Other STEM',
    'Early Care and Education': 'Education',
    'Earth Science': 'Other STEM',
    'Earth Science Interdept': 'Other STEM',
    'East Asian Languages & Culture': 'Non STEM',
    'Economic Geography': 'Other STEM',
    'Economics': 'Non STEM',
    'Education': 'Education',
    'Electrical Engineering': 'Engineering',
    'Electrical Technology': 'Other STEM',
    'Elementary Education': 'Education',
    'Engineering   No Preference': 'Engineering',
    'Engineering Arts': 'Engineering',
    'Engineering Mechanics': 'Engineering',
    'English': 'Non STEM',
    'English Language Center': 'Non STEM',
    'Entomology': 'Other STEM',
    'Envir & Natural Res Policy Std': 'Other STEM',
    'Envir Biol/Botany & Plant Path': 'Other STEM',
    'Envir Biology/Microbiology': 'Other STEM',
    'Envir Biology/Plant Biology': 'Other STEM',
    'Envir Studies & Sustainability': 'Other STEM',
    'Envir Studies and Agriscience': 'Other STEM',
    'Environ Biology/Microbiology': 'Other STEM',
    'Environ Studies & Applications': 'Other STEM',
    'Environmental Biol/Plant Biol': 'Other STEM',
    'Environmental Biology/Botany': 'Other STEM',
    'Environmental Biology/Zoology': 'Other STEM',
    'Environmental Economics & Mgt': 'Other STEM',
    'Environmental Economics&Policy': 'Other STEM',
    'Environmental Engineering': 'Engineering',
    'Environmental Geography': 'Other STEM',
    'Environmental Geosciences': 'Other STEM',
    'Environmental Sci & Mgt': 'Other STEM',
    'Environmental Soil Science': 'Other STEM',
    'Epidemiology': 'Other STEM',
    'Experience Architecture': 'Non STEM',
    'Family & Consumer Resources': 'Non STEM',
    'Family Community Services': 'Non STEM',
    'Family and Consumer Sciences': 'Non STEM',
    'Film Studies': 'Non STEM',
    'Finance': 'Other STEM',
    'Financial Administration': 'Non STEM',
    'Fisheries and Wildlife': 'Other STEM',
    'Food Industry Management': 'Non STEM',
    'Food Science': 'Other STEM',
    'Food: Technology & Management': 'Non STEM',
    'Forensic Science': 'Other STEM',
    'Forestry': 'Other STEM',
    'French': 'Non STEM',
    'Fruit & Vegetable Crop Mgt': 'Other STEM',
    'General Business Admin': 'Non STEM',
    'General Business Admin Prelaw': 'Non STEM',
    'General Management': 'Non STEM',
    'General Science': 'Other STEM',
    'General Science Interdept': 'Other STEM',
    'Genomics & Molecular Genetics': 'Other STEM',
    'Geographic Information Science': 'Other STEM',
    'Geography': 'Other STEM',
    'Geological Sciences': 'Other STEM',
    'Geology': 'Other STEM',
    'Geophysics': 'Other STEM',
    'German': 'Non STEM',
    'Global & Area Studies Soc Sci': 'Other STEM',
    'Global & Intl Stdys in Soc Sci': 'Other STEM',
    'Global Stdys Arts & Humanities': 'Non STEM',
    'Graphic Design': 'Other STEM',
    'High School Guest': 'Other/Guest/HS-student',
    'Hist,Philosophy & Soc of Sci': 'Non STEM',
    'History': 'Non STEM',
    'History Education': 'Education',
    'History of Art': 'Non STEM',
    'Home Economics': 'Non STEM',
    'Horse Management': 'Non STEM',
    'Horticulture': 'Other STEM',
    'Hospitality Business': 'Non STEM',
    'Hotel & Restaurant Management': 'Non STEM',
    'Human Biology': 'Other STEM',
    'Human Devel and Family Studies': 'Non STEM',
    'Human Devl and Family Studies': 'Non STEM',
    'Human Geography': 'Other STEM',
    'Human Medicine': 'Other STEM',
    'Human Resource Management': 'Non STEM',
    'Human Resources and Labor Rel': 'Non STEM',
    'Humanities': 'Non STEM',
    'Humanities Prelaw': 'Non STEM',
    'Industrial Mathematics': 'Other STEM',
    'Instrumental Music Education': 'Education',
    'Integrative Biology': 'Other STEM',
    'Integrative Pharmacology': 'Other STEM',
    'Interdisciplinary Humanities': 'Non STEM',
    'Interior Design': 'Non STEM',
    'Interior Design&Facilities Mgt': 'Non STEM',
    'International Relations': 'Non STEM',
    'Intr Stdy S S Public Plcy Stdy': 'Other STEM',
    'Intr Stdy Soc Sci Cmty Rel': 'Other STEM',
    'Intr Stdy Soc Sci Envir Policy': 'Other STEM',
    'Intr Stdy Soc Sci Health Stdy': 'Other STEM',
    'Intr Stdy Soc Sci Hm Res Scty': 'Other STEM',
    'Intr Stdy Soc Sci Human Aging': 'Other STEM',
    'Intr Stdy Soc Sci Intl Studies': 'Other STEM',
    'Intr Stdy Soc Sci Law&Society': 'Other STEM',
    'Intr Stdys Soc Sci: Soc Sci Ed': 'Other STEM',
    'Intr Studies in Social Science': 'Other STEM',
    'James Madison': 'Non STEM',
    'Japanese': 'Non STEM',
    'Jazz Studies': 'Non STEM',
    'Journalism': 'Non STEM',
    'Kinesiology': 'Other STEM',
    'LBS   No Coordinate Major': 'LBS',
    'LBS Animal Science': 'LBS',
    'LBS Astrophysics': 'LBS',
    'LBS Biochem and Molecular Biol': 'LBS',
    'LBS Biochemistry': 'LBS',
    'LBS Biochemistry/Biotechnology': 'LBS',
    'LBS Biological Science': 'LBS',
    'LBS Biology Field of Concent': 'LBS',
    'LBS Botany and Plant Pathology': 'LBS',
    'LBS Chemical Physics': 'LBS',
    'LBS Chemistry': 'LBS',
    'LBS Computational Chemistry': 'LBS',
    'LBS Computational Mathematics': 'LBS',
    'LBS Computer Science': 'LBS',
    'LBS Computer Science   FC': 'LBS',
    'LBS Earth Science   FC': 'LBS',
    'LBS Earth Science Interdept': 'LBS',
    'LBS Entomology': 'LBS',
    'LBS Envir Biology/Plant Biol': 'LBS',
    'LBS Envir Biology/Zoology': 'LBS',
    'LBS Envir/Bio/Botany & Plant P': 'LBS',
    'LBS Envir/Biology/Microbiology': 'LBS',
    'LBS Environ Sci and Management': 'LBS',
    'LBS Environmental Geosciences': 'LBS',
    'LBS General Science Interdept': 'LBS',
    'LBS Genomics & Molecular Genet': 'LBS',
    'LBS Geological Sciences': 'LBS',
    'LBS Human Biology': 'LBS',
    'LBS Mathematics': 'LBS',
    'LBS Medical Technology': 'LBS',
    'LBS Microbiology': 'LBS',
    'LBS Nutritional Sciences': 'LBS',
    'LBS Physical Science   FC': 'LBS',
    'LBS Physical Science Interdept': 'LBS',
    'LBS Physics': 'LBS',
    'LBS Physics and Geophysics': 'LBS',
    'LBS Physiology': 'LBS',
    'LBS Plant Biology': 'LBS',
    'LBS Science & Tech Studies  FC': 'LBS',
    'LBS Statistics': 'LBS',
    'LBS Zoology': 'LBS',
    'Landscape Architecture': 'Non STEM',
    'Landscape Management': 'Non STEM',
    'Landscape and Lawn Management': 'Non STEM',
    'Landscape and Nursery': 'Non STEM',
    'Landscape and Nursery Mgt': 'Non STEM',
    'Language Program': 'Non STEM',
    'Latin': 'Non STEM',
    'Law': 'Non STEM',
    'Law Non Degree Guest': 'Other/Guest/HS-student',
    'Lifelong Education': 'Education',
    'Linguistics': 'Non STEM',
    'Livestock Industries': 'Non STEM',
    'Lyman Briggs': 'LBS',
    'Lyman Briggs School': 'LBS',
    'MLM Logistics': 'Non STEM',
    'Management': 'Non STEM',
    'Management,Strategy,Leadership': 'Non STEM',
    'Manufacturing Engineering': 'Non STEM',
    'Marketing': 'Non STEM',
    'Materials Sci and Engineering': 'Engineering',
    'Mathematics': 'Other STEM',
    'Mathematics Education': 'Education',
    'Mathematics, Advanced': 'Other STEM',
    'Mechanical Engineering': 'Engineering',
    'Mechanics': 'Engineering',
    'Media Arts and Technology': 'Other STEM',
    'Media and Communication Tech': 'Other STEM',
    'Media and Information': 'Non STEM',
    'Medical Technology': 'Non STEM',
    'Merchandising Management': 'Non STEM',
    'Microbiol & Molecular Genetics': 'Other STEM',
    'Microbiology': 'Other STEM',
    'Music': 'Non STEM',
    'Music   No Major': 'Non STEM',
    'Music Education': 'Education',
    'Music Performance': 'Non STEM',
    'Music Therapy': 'Non STEM',
    'Natural Res Recreation & Tour': 'Other STEM',
    'Natural Science No Preference': 'Other STEM',
    'Neuroscience': 'Other STEM',
    'No Preference': 'No Preference',
    'Nursing': 'Other STEM',
    'Nutritional Sciences': 'Other STEM',
    'Organic Farming': 'Other STEM',
    'Osteopathic Medicine': 'Other STEM',
    'Packaging': 'Engineering',
    'Park and Recreation Resources': 'Non STEM',
    'Park, Recreation & Tourism Res': 'Non STEM',
    'Personnel Administration': 'Non STEM',
    'Pharmacology & Toxicology': 'Other STEM',
    'Philosophy': 'Non STEM',
    'Phys Ed & Exercise Science': 'Education',
    'Physical Education': 'Education',
    'Physical Science': 'Other STEM',
    'Physical Science Interdept': 'Other STEM',
    'Physics': 'Physics',
    'Physics and Geophysics': 'Other STEM',
    'Physiology': 'Other STEM',
    'Plant Biology': 'Other STEM',
    'Plant Breeding & Genetics CSS': 'Other STEM',
    'Plant Pathology': 'Other STEM',
    'Pol Theory&Constitutional Dem': 'Non STEM',
    'Policy and Applied Economics': 'Non STEM',
    'Political Economy': 'Non STEM',
    'Political Science': 'Non STEM',
    'Political Science Prelaw': 'Non STEM',
    'Predental': 'Other STEM',
    'Premedical': 'Other STEM',
    'Prenursing': 'Other STEM',
    'Preoptometry': 'Other STEM',
    'Preveterinary': 'Other STEM',
    'Professional Writing': 'Non STEM',
    'Psychology': 'Other STEM',
    'Public Admin and Public Policy': 'Non STEM',
    'Public Administration': 'Non STEM',
    'Public Affairs Management': 'Non STEM',
    'Public Health': 'Other STEM',
    'Public Policy': 'Non STEM',
    'Public Resource Management': 'Non STEM',
    'Recreation and Youth Leadershp': 'Education',
    'Religious Studies': 'Non STEM',
    'Residential Coll in Arts & Hum': 'Non STEM',
    'Resource Development': 'Non STEM',
    'Retailing': 'Non STEM',
    'Russian': 'Non STEM',
    'School Music   No Major': 'Non STEM',
    'School Psychology': 'Other STEM',
    'Science & Technology Studies': 'Other STEM',
    'Social Relations': 'Non STEM',
    'Social Relations and Policy': 'Non STEM',
    'Social Science': 'Non STEM',
    'Social Science Law, Democracy': 'Non STEM',
    'Social Science Prelaw': 'Non STEM',
    'Social Work': 'Non STEM',
    'Sociology': 'Non STEM',
    'Spanish': 'Non STEM',
    'Special E Emotional Impairment': 'Education',
    'Special Ed Deaf Education': 'Education',
    'Special Ed Learn Disabilities': 'Education',
    'Special Ed Visual Impairment': 'Education',
    'Sports and Commercial Turf Mgt': 'Non STEM',
    'Statistics': 'Other STEM',
    'Stringed Instrument Music Ed': 'Education',
    'Studio Art': 'Non STEM',
    'Supply Chain Management': 'Non STEM',
    'Sustainable Parks,Rec and Tour': 'Non STEM',
    'Swine Management': 'Other STEM',
    'Teaching Cert Internship Year': 'Non STEM',
    'Teaching and Curriculum': 'Education',
    'Technology Systems Management': 'Other STEM',
    'Telecomm, Info Studies & Media': 'Non STEM',
    'Telecommunication': 'Other STEM',
    'Theatre': 'Non STEM',
    'Transient Major': 'Other/Guest/HS-student',
    'Turfgrass Management': 'Non STEM',
    'Turfgrass Management Golf': 'Non STEM',
    'Urban and Regional Planning': 'Other STEM',
    'Veterinary Medicine': 'Other STEM',
    'Veterinary Technology': 'Other STEM',
    'Viticulture': 'Other STEM',
    'Vocal General Music Education': 'Education',
    "Women's Studies": 'Non STEM',
    "Women's and Gender Studies": 'Non STEM',
    'World Politics': 'Non STEM',
    'Zoology': 'Other STEM'}

    major = str.rstrip(str.lstrip(major))
    return major_category_lookup[major]

if __name__=="__main__":
    # do all the functions on input files
    # write new columns to files