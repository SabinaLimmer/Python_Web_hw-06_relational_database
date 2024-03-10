--Średnia ocen dla wszystkich grup, uwzględniając wszystkie oceny.
SELECT students.group_id, AVG(grade) AS average_grade
FROM grades
JOIN students ON grades.student_id = students.id
GROUP BY students.group_id;