# Create a function called: calculate_avg_grade
# Parameters: the function should receive 1 parameter: a list of student objects
#             Remember a list can contain duplicates, so you can expect two student objects with same ID but different grades
# Returns: the function should return a dictionary with student ID as key and student average grade as value
#
# Example:
# input: [Student('s1',20,1824,90.5), Student('s2',21,1823,80.0), Student('s1',20,1824,70.0)]
# output: { 1824: 80.25, 1823: 80.0 }
#
# If the list of students is empty, return an empty dictionary
# Make sure that you add type hints to the function paramter and return value
from app.src.utils import calculate_avg
from app.src.Student import Student


def calculate_avg_grade(students: list[Student]) -> dict[int, float]:
    if students == {}:
        return {}
    
    grades_id: dict[int, list[Student]] = {}
    for student in students:
        if grades_id.get(student.id) == None:
            grades_id[student.id] = [student.grade]
        else:
            grades_id[student.id].append(student.grade)

    gpa_id: dict[int, float] = {}
    for id, grades in grades_id.items():
        gpa_id[id] = calculate_avg(grades)
    return gpa_id