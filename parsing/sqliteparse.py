from lark import Lark, Transformer
import sqlite3

# ---------- ГРАММАТИКА ----------
grammar = """
    start: expr

    ?expr: expr "and" expr   -> and_expr
         | expr "or" expr    -> or_expr
         | "(" expr ")"
         | condition

    condition: FIELD OPERATOR value

    value: SIGNED_NUMBER    -> number
         | ESCAPED_STRING   -> string

    FIELD: /[a-zA-Z_][a-zA-Z0-9_]*/
    OPERATOR: "==" | "!=" | ">" | "<" | ">=" | "<="

    %import common.SIGNED_NUMBER
    %import common.ESCAPED_STRING
    %import common.WS
    %ignore WS
"""

parser = Lark(grammar)


# ---------- ПРЕОБРАЗОВАТЕЛЬ ----------
class ToSQL(Transformer):
    def start(self, args):
        # Получаем сразу SQL-условие, не оборачивая в Tree
        return args[0]

    def and_expr(self, args):
        return f"({args[0]} AND {args[1]})"

    def or_expr(self, args):
        return f"({args[0]} OR {args[1]})"

    def condition(self, args):
        field, op, value = args
        return f"{field} {op} {value}"

    def number(self, args):
        return args[0].value

    def string(self, args):
        # args[0].value уже содержит строку с кавычками, например '"Moscow"'
        return args[0].value

    def FIELD(self, token):
        return token.value

    def OPERATOR(self, token):
        op = token.value
        # В SQL для равенства используем одинарный знак =
        if op == "==":
            return "="
        return op


# ---------- СОЗДАНИЕ БАЗЫ ----------
def create_db():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE people (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            city TEXT
        )
    """)
    people = [
        ("Alice", 25, "Moscow"),
        ("Bob", 30, "London"),
        ("Charlie", 22, "Moscow"),
        ("Dave", 19, "New York"),
    ]
    cur.executemany("INSERT INTO people (name, age, city) VALUES (?, ?, ?)", people)
    conn.commit()
    return conn


# ---------- ПОИСК ----------
def search_people(conn, query_text):
    tree = parser.parse(query_text)
    print("Дерево после разбора:")
    print(tree.pretty())

    # Трансформируем в строку SQL-условия
    sql_condition = ToSQL().transform(tree)

    sql = f"SELECT name, age, city FROM people WHERE {sql_condition}"
    print("SQL запрос:")
    print(sql)

    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()


# ---------- ПРИМЕР ИСПОЛЬЗОВАНИЯ ----------
if __name__ == "__main__":
    conn = create_db()
    query = 'age > 20 and city == "Moscow"'
    results = search_people(conn, query)

    for name, age, city in results:
        print(f"{name}, {age} years old, from {city}")
