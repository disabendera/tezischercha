----------------------------- MODULE operators -----------------------------
EXTENDS Integers

MinutesToSeconds(m) == m * 60
Abs(x) == IF x < 0 THEN -x ELSE x
Xor(A, B) == A = ~B

a == MinutesToSeconds(10)
b == Abs(-10)
c == IF Xor(TRUE, FALSE) THEN 1 ELSE 0

=============================================================================
\* Modification History
\* Last modified Sat Apr 26 19:13:24 KRAT 2025 by highy
\* Created Sat Apr 26 19:07:28 KRAT 2025 by highy
