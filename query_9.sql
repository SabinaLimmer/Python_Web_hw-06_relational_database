--Lista kursów, na które uczęszcza uczeń.
 SELECT subjects.subject_name
 FROM subjects
 JOIN grades ON subjects.id = grades.subject_id
 WHERE grades.student_id = 1;