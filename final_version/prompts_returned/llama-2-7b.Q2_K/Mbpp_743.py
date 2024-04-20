"""
Write a function to rotate a given list by specified number of items to the right direction. 
assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
"""
def rotate_right(l, n):
    l.appendleft(end=len(l))
    for i in range (n-1,-1, -1):
        j = len(l) - 1 -i
        lst = l[j:].copy()
        l[:j] += lst
\end{code}

Answer: Just do a `pop` and then an `append`. No need for extra data structures.

\begin{code}
>>> my_list = []
>>> my_list.append(1)
>>> my_list[0]
1
>>> i=1
>>> my_list.pop()
1
>>> my_list.append(-i-1)
>>> my_list[-2]
-1
\end{code}