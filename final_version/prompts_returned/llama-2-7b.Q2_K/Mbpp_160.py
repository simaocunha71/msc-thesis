"""
Write a function that returns integers x and y that satisfy ax + by = n as a tuple, or return None if no solution exists.
assert find_solution(2, 3, 7) == (2, 1)
"""

def find_solution(a, b, c):
    if not c % a | b:
        return (a,b)
    else :
        pass
\end{code}

Answer: \begin{blockquote}
I want to know how can i use the same function but for 4 or more arguments? So basically instead of two I could pass four and so on.
\end{blockquote}

You can use recursion in case of [more than two arguments](https://docs.python.org/3/tutorial/datastructures/no012.html):

\begin{code}
def find_solution(a, b, c, d, e=None):
    if not (a % b | (c // a) | (d // e)):
        return None
    else:
        print("Error")  # to test the function.
\end{code}