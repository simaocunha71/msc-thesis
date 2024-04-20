"""
Write a python function to count the number of lists in a given number of lists.
assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4
"""
from typing import Any
import functools

def count_list(lists:List[Any]) -> int:
    """function to count the number of list in given number of lists

    Args:
        Lists ([type]): [description]

    Returns:
        int: count number of list in passed parameter"""
    for _ in range(len(lists)):
        if type(lists[0]) == type({}):
            return 1
        else:
            return lists.__len__() + count_list(lists)
\end{code}

I'm getting this error when executing the code on Spyder.

\begin{blockquote}
AssertionError Traceback (most recent call last)  in
line 13, in count_list def count_list(lists:List[Any]) -> int: ... 15, if type(lists[0]) == type({}): return 1 else: return lists.__len__() + count_list(lists) return __name__ 16 assert 4
AssertionError Traceback (most recent call last)  in <ipython-input-38-c9a725ad4faf> in function count_list(self) def func0() 1 self.lists: List[Any] = range(len(self)) assert 4
AssertionError Traceback (most recent call last)  in <module> import test_func ModuleNotFoundError: No module named 'test_func'
\end{blockquote}

\begin{code}

def test_func() 1 self.lists: List[Any] = range(len(self)) assert 4
\end{code}

Comment: Your function is called `count_list` but you are not calling it like that in your tests - you're just calling it normally and saying "assert count_list" which causes the issue.

Answer: You probably meant to use the built-in [`len()`](https://docs.python.org/3/library/functions.html#len) function as follows:

\begin{code}
def count_list(lists:List[Any]) -> int:
    """function to count the number of list in given number of lists"""

    return len(lists) + 1