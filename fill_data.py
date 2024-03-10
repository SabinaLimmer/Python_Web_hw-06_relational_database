from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUMBER_STUDENTS = 30
NUMBER_GROUPS = 3
NUMBER_SUBJECTS = 5
NUMBER_LECTURERS = 3
GRADES_SCOPE = [
    2,
    3,
    4,
    5,
]
SUBJECTS_NAMES = [
    "Math", 
    "Physics", 
    "Chemistry", 
    "Biology", 
    "History",
]
    

def generate_fake_data(number_students, number_groups, number_subjects, number_lecturers, grades_scope, subjects_names) -> tuple:
    fake_students = []
    fake_subjects = []
    fake_lecturers = []
    fake_grades = []
    fake_data = faker.Faker()

    for _ in range(number_students):
        fake_students.append((fake_data.name(), randint(1, number_groups)))
    
    for _ in range(number_subjects):
        fake_subjects.append((subjects_names[_], randint(1, number_lecturers)))

    for _ in range(number_lecturers):
        fake_lecturers.append((fake_data.name(),))

    for student_id in range(1, number_students + 1):
        for _ in range(randint(15, 20)):
            grade_date = datetime(2024, 1, randint(2, 31)).date()
            fake_grades.append(
                (
                    choice(grades_scope),
                    grade_date,
                    randint(1, len(fake_subjects)),
                    student_id,
                )
            )

    return fake_students, fake_subjects, fake_lecturers, fake_grades


def insert_data_to_db(students, subjects, lecturers, grades, groups) -> None:
    with sqlite3.connect('mysql.db') as con:
        cur = con.cursor()

        sql_to_students = """INSERT INTO students(student_name, group_id)
                               VALUES (?, ?)"""
        cur.executemany(sql_to_students, students)

        sql_to_subjects = """INSERT INTO subjects(subject_name, lecturer_id)
                               VALUES (?, ?)"""
        cur.executemany(sql_to_subjects, subjects)

        sql_to_lecturers = """INSERT INTO lecturers(lecturer_name)
                              VALUES (?)"""
        cur.executemany(sql_to_lecturers, lecturers)

        sql_to_grades = """INSERT INTO grades(grade, date_of, subject_id, student_id)
                              VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_grades, grades)

        sql_to_groups = """INSERT INTO groups(group_number)
                              VALUES (?)"""
        cur.executemany(sql_to_groups, groups)

        con.commit()

if __name__ == "__main__":
    students, subjects, lecturers, grades = generate_fake_data(NUMBER_STUDENTS, NUMBER_GROUPS, NUMBER_SUBJECTS, NUMBER_LECTURERS, GRADES_SCOPE, SUBJECTS_NAMES)
    groups = [(group_number,) for group_number in range(1, NUMBER_GROUPS + 1)]
    insert_data_to_db(students, subjects, lecturers, grades, groups)