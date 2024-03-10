-- Zaimplementuj bazę danych, która ma schemat zawierający:
-- Wypełnij bazę danych danymi losowymi (~30-50 uczniów, 3 grupy, 5-8 przedmiotów, 3-5 wykładowców, do 20 ocen dla każdego ucznia ze wszystkich przedmiotów). W tym celu użyj pakietu Faker.

-- Tabelę ze studentami;
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name VARCHAR(100) NOT NULL,
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);

-- Tabelę z grupami;
DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_number INTEGER NOT NULL
);

-- Tabelę z wykładowcami;
DROP TABLE IF EXISTS lecturers;
CREATE TABLE lecturers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lecturer_name VARCHAR(100) NOT NULL
);

-- Tabelę z przedmiotami wraz z podaniem wykładowcy, który prowadzi dany przedmiot;
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name VARCHAR(30) NOT NULL,
    lecturer_id INTEGER,
    FOREIGN KEY (lecturer_id) REFERENCES lecturers (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);

-- Tabelę, zawierającą oceny z poszczególnych przedmiotów dla każdego ucznia wraz z datą, kiedy ocena została wystawiona;
DROP TABLE IF EXISTS grades;
CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    grade INTEGER NOT NULL,
    date_of DATE NOT NULL,
    student_id INTEGER,
    subject_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);
