--Lista kursów prowadzonych przez wybranego wykładowcę dla określonego ucznia.
SELECT subjects.subject_name
FROM subjects
JOIN grades ON subjects.id = grades.subject_id
JOIN students ON grades.student_id = students.id
WHERE subjects.lecturer_id = 1 AND students.id = 1;