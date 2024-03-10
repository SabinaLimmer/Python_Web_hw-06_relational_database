--5 uczniów z najwyższą średnią ocen ze wszystkich przedmiotów.
SELECT student_id, AVG(grade) AS average_grade
FROM grades
GROUP BY student_id
ORDER BY average_grade DESC
LIMIT 5;