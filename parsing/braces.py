from lark import Lark

grammar = """
    start: pair*

    pair: "(" pair* ")" 
        | "[" pair* "]" 
        | "{" pair* "}"
"""

parser = Lark(grammar)

# Проверим:
good = "({[]})"
bad = "({[})"

print("good:", parser.parse(good))
try:
    parser.parse(bad)
except Exception as e:
    print("bad:", e)
