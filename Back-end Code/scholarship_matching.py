"""
This file contains the main functionality for matching a student with a list of scholarships,
sorted from top to bottom in terms of relevance (from high to low).
"""

import string
import json


def match_scholarship(stu_email: string) -> [string]:
    """
    Given a Student's email (which functions as UUID for the student),
    it matches the student with a list of Scholarships (UUIDs) that the function recommends, sorted
    by relevance (high to low).
    """

    student_file = open('data/students.json')
    s_data = json.load(student_file)
    for student in s_data:
        if student["email"] == stu_email:
            s_institution = student["institution"]
            s_faculty = student["faculty"]
            s_interests = student["interests"]
            s_description = student["description_of_self"]

            return find_scholarships_for_student(s_institution, s_faculty, s_interests,
                                                 s_description)

    return []  # no such student is found, default empty return as ERROR handling


def find_scholarships_for_student(s_institution: string, s_faculty: string, s_interests: [string],
                                  s_description: string) -> [string]:
    """Helper function to match_scholarship; finds a list of scholarships (UUIDs)
    """
    scholarship_file = open('data/scholarships.json')
    scholarship_data = json.load(scholarship_file)

    shortlist = []

    for s in scholarship_data:
        if s["criteria_institution"] == s_institution and s["criteria_faculty"] == s_faculty:
            shortlist.append(s["UUID"])

    # TODO: Sort the shortlisted scholarships by relevance

    return shortlist
