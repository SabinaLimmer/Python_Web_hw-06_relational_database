--Średnia ocen wystawionych przez wykładowcę z danego przedmiotu.
SELECT AVG(grade) AS average_grade
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
WHERE subjects.lecturer_id = 1 AND grades.subject_id = 3;