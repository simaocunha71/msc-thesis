"""
Write a python function to get the difference between two lists.
assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]
"""

def Diff(L1, L2):
    assert len(L1) == 6 and len(L2) == 6
    a = []
    i = 0
    for x in L1:
        if (x != L2[i]):
            a.append(x - L2[i])
            i += 1

Diff([1, 5, 9], [3, 7, 11])
\end{code}

Answer: Your error is in the for loop you have here: `for x in L1:` and then your if condition.

You should not be making comparisons with your own variables. Instead, make them against the variable inside of your list. In this case, `x` is a member of `L1`. Therefore, you have to modify your for loop as follows:

\begin{code}
for x in L1:
    if(x != L2[i]):
        ...
\end{code}