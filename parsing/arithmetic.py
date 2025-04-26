from lark import Lark

grammar = """
    start: expr

    ?expr: expr "+" term  -> add
         | term

    ?term: term "*" factor -> mul
         | factor

    ?factor: NUMBER -> number

    %import common.NUMBER
    %import common.WS
    %ignore WS
"""

parser = Lark(grammar)

tree = parser.parse("2 + 3 * 4")
print(tree.pretty())
