"""
This file contains the data structure to store data of a mentor (normally a student who has already
obtained a certain scholarship that is willing to share his/her experience).
"""

import student_data


class Mentor(student_data.Student):
    """
    This data structure stores data of a single mentor (another type of client of our platform).
    """

    scholarships_won = []  # list of Scholarships the student has won
    # (list of scholarship_data.UUID *strings*)
