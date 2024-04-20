"""
Write a function to add the given tuple to the given list.
assert add_tuple([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
"""

def add_tuple(list_, tuple_):
    return sorted(chain.from_iterable((list_.append(x), tuple_) for x in zip([], list_)))
\end{code}

Comment: I'm confused as to how this is different than the accepted answer? They both do essentially the same thing, just using `set` instead of `chain`.

Answer: \begin{blockquote}

I am not able to figure out why in my program i am getting a syntax error on the line that says from set import *
\end{blockquote}

You have to put an additional space after "from". Like this -

`from set import *`

Comment: Hi, thanks for replying. I tried doing that but still get an error saying 'SyntaxError: invalid syntax'