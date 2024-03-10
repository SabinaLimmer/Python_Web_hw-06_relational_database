--Średnia ocen w grupach dla wybranego przedmiotu.
SELECT students.group_id, AVG(grades.grade) AS average_grade
FROM grades
JOIN students ON grades.student_id = students.id
WHERE grades.subject_id = 1
GROUP BY students.group_id;