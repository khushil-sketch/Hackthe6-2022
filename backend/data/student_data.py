"""
This file contains the data structure to store data of a student
"""

import string
from geopy.geocoders import Nominatim
import json


class Student:
    """
    This data structure stores data of a single student (main client type of our platform).
    """
    name = ""  # name of the student
    email = ""  # email address of the student (USED AS UNIQUE ID)
    password = ""  # password of this account (INSECURE, DEMO ONLY)
    address = ""  # address of student, used for location generation

    institution = ""  # name of school the student studies, or desires to study under
    faculty = ""  # specific faculty (i.e. major or direction of study) the student is pursuing
    interests = []  # list of interests the student has (FOR KEYWORD SEARCHING)
    description_of_self = ""  # student's description of oneself (FOR KEYWORD MATCHING)

    location = None  # location of student, for mentor pairing

    def __init__(self, name: string, email: string, password: string, address: string,
                 institution: string, faculty: string, interests: [string], description: string):
        self.name = name
        self.email = email
        self.password = password
        self.address = address
        self.institution = institution
        self.faculty = faculty
        self.interests = interests
        self.description_of_self = description

        # initialize student location
        geolocator = Nominatim(user_agent="ProjectS")
        self.location = geolocator.geocode(address).raw
        # print(self.location)


def generate_sample_data() -> None:
    """
    This function generates a sample json file that is available for usage.
    """
    # sample list of students
    temp = [Student("John Doe", "john.doe@gmail.com", "I<3UofT", "Toronto",
                    "University of Toronto", "Engineering", ["Football", "Music"],
                    "Hi I am interested in Engineering."),
            Student("Jane Appleseed", "jane123@gmail.com", "87654321", "Montreal",
                    "York University", "Engineering", ["Language Learning"],
                    "Hi I am also interested in Engineering.")
            ]

    s_list = []
    for student in temp:
        s_list.append(student.__dict__)

    with open("students.json", "w") as file:
        json.dump(s_list, file)


# This function is for TESTING ONLY
if __name__ == "__main__":
    # student1 = Student("John Doe", "john.doe@gmail.com", "I<3UofT", "Toronto",
    #                    "University of Toronto", "Engineering", ["Football", "Music"],
    #                    "Hi I am interested in Engineering.")
    # student2 = Student("Jane Appleseed", "jane123@gmail.com", "87654321", "Montreal",
    #                    "York University", "Engineering", ["Language Learning"],
    #                    "Hi I am also interested in Engineering.")
    #
    # json_student1 = json.dumps(student1.__dict__)
    # json_student2 = json.dumps(student2.__dict__)
    #
    # print(json_student1)
    # print(json_student2)

    generate_sample_data()
