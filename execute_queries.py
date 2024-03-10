import sqlite3

QUERIES = {
    1: "5 uczniów z najwyższą średnią ocen ze wszystkich przedmiotów.",
    2: "Uczeń z najwyższą średnią ocen z wybranego przedmiotu.",
    3: "Średnia ocen w grupach dla wybranego przedmiotu.",
    4: "Średnia ocen dla wszystkich grup, uwzględniając wszystkie oceny.",
    5: "Przedmioty, które prowadzi wybrany wykładowca.",
    6: "Lista uczniów w wybranej grupie.",
    7: "Oceny uczniów w wybranej grupie z określonego przedmiotu.",
    8: "Średnia ocen wystawionych przez wykładowcę z danego przedmiotu.",
    9: "Lista kursów, na które uczęszcza uczeń.",
    10: "Lista kursów prowadzonych przez wybranego wykładowcę dla określonego ucznia.",
}

def execute_query(sql_query):
    with sqlite3.connect('mysql.db') as con:
        cur = con.cursor()
        cur.execute(sql_query)
        return cur.fetchall()

def sql_query(file_query_number):
    with open(file_query_number, "r") as f:
        sql = f.read()
    return sql

if __name__ == "__main__":
    for number, query in QUERIES.items():
        print(f"Zadanie {number}: {query}")
        print(execute_query(sql_query(f"query_{number}.sql")))
        print("\n")