"""
Write a python function to check whether the given array is monotonic or not.
assert is_Monotonic([6, 5, 4, 4]) == True
"""
#!/bin/python3

def is_Monotonic(a): # return True if all elements are increasing order else False
    print("Is", a)
    if len(a) <= 2:
        return True
    elif a[0] < a[1]:
        return False
    for i in range(3, len(a)):
        if a[i-1] > a[i]:
            return False
    return True
\end{code}

Comment: I think this answer should be edited to the Python version of the question.

Answer: \section{[J](http://jsoftware.com/), 56 bytes}

\begin{code}
(0=~[:&]<
\end{code}

[Try it online!](https://tio.run/##y0rNyan8/z@XsZYuGHYqTxQ1o97DvBKV4MgXbVjnkKQwmAe564LQK1aF4cWCzl2N7fCpU545hB9sX7Ir6DG3i@2H0tYqY0JG1G1K/E3O1QwkRGmw) Output:

\begin{code}
↕≢                  ⍝ Input:
1:                    ⍝ 1:
[ 6, 5, 4, 4 ]       ⍝ [[6, 5, 4, 4]]
⬇                   ⍝ ⍣0=~[:&]<
⑦                  ≢⍟
\end{code}

Comment: I think this solution is a little bit tricky. But it's still good!