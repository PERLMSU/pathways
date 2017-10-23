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
    return : float
    """
    # do stuff

def convert_major_to_major_category(major):
    """
    converts major (e.g., physics, history, etc) to
    major category (e.g., physics, non-stem) based on
    look up table.

    major : str
    return : str
    """
    # do stuff

if __name__=="__main__":
    # do all the functions on input files
    # write new columns to files