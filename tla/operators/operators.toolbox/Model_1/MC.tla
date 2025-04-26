---- MODULE MC ----
EXTENDS operators, TLC

\* Constant expression definition @modelExpressionEval
const_expr_174566962050725000 == 
a + b + c
----

\* Constant expression ASSUME statement @modelExpressionEval
ASSUME PrintT(<<"$!@$!@$!@$!@$!",const_expr_174566962050725000>>)
----

=============================================================================
\* Modification History
\* Created Sat Apr 26 19:13:40 KRAT 2025 by highy
