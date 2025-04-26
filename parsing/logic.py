from lark import Lark

grammar = """
    start: expr

    ?expr: or_expr

    ?or_expr: and_expr
            | or_expr OR and_expr -> or_op

    ?and_expr: atom
             | and_expr AND atom -> and_op

    ?atom: TRUE    -> true
         | FALSE   -> false
         | "(" expr ")"

    TRUE: "True"
    FALSE: "False"
    AND: "and"
    OR: "or"

    %import common.WS
    %ignore WS
"""

parser = Lark(grammar)

tree = parser.parse("True and (False or True)")
print(tree.pretty())
