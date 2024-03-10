--Oceny uczniów w wybranej grupie z określonego przedmiotu.
SELECT student_name, grade
FROM students
JOIN grades ON students.id = grades.student_id
WHERE students.group_id = 1 AND grades.subject_id = 1;
