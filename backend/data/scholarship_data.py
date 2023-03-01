"""
This file contains the data structure to store a scholarship listing
"""
import string
import json
import uuid


class Scholarship:
    """
    This data structure stores information about a single scholarship listing.
    """
    UUID = ""  # unique ID for the scholarship

    name = ""  # name of award
    description = ""  # brief description of award (CAN BE EXTRACTED FOR KEYWORDS)
    donor = ""  # name of donor, can be schools, public/private organizations, private persons
    amount = 0  # 0 means variable amount; -1 means FULL scholarship; positive int means specific

    criteria_origin = "DI"  # "D" for domestic, "I" for international, "DI" for both
    criteria_institution = ""  # institution the student must be studying under in order to apply;
    # leave blank for any
    criteria_faculty = ""  # further restriction on faculty the student is studying under within the
    # institution, leave blank ("") for any

    def __init__(self, name: string, description: string, donor: string, amount: int,
                 origin: string, institution: string, faculty: string) -> None:
        self.name = name
        self.description = description
        self.donor = donor
        self.amount = amount
        self.criteria_origin = origin
        self.criteria_institution = institution
        self.criteria_faculty = faculty

        self.UUID = str(uuid.uuid5(uuid.NAMESPACE_DNS, (self.name + self.description)))


def generate_sample_data() -> None:
    """
    This function generates a sample json file that is available for usage.
    """
    # sample list of scholarships
    temp = [Scholarship("U of T Scholar",
                        "This scholarship is awarded for students within University of Toronto.",
                        "University of Toronto Fund", 1500, "DI", "University of Toronto", ""),
            Scholarship("York Engineer Award",
                        "This scholarship is awarded for Engineering students that excel.",
                        "York University", 2000, "DI", "York University", "Engineering")
            ]

    s_list = []
    for scholarship in temp:
        s_list.append(scholarship.__dict__)

    with open("scholarships.json", "w") as file:
        json.dump(s_list, file)


# This function is for TESTING ONLY
if __name__ == "__main__":
    # scholar1 = Scholarship("U of T Scholar",
    #                        "This scholarship is awarded for students in University of Toronto.",
    #                        "University of Toronto Fund", 1500, "DI", "University of Toronto", "")
    # scholar2 = Scholarship("York Engineer Award",
    #                        "This scholarship is awarded for Engineering students that excel.",
    #                        "York University", 2000, "DI", "York University", "Engineering")
    #
    # json_scholar1 = json.dumps(scholar1.__dict__)
    # json_scholar2 = json.dumps(scholar2.__dict__)
    #
    # print(json_scholar1)
    # print(json_scholar2)

    generate_sample_data()
