"""
Write a python function to find the first digit of a given number.
assert first_Digit(123) == 1
"""

def first_digit(num):
    if num<0 or len(str(num))==0:
        return -9999

    while (len(str(num))>0 and str(num)[-1]!='0'):
        num=str(num)[:-1]+'0'+str(num)

    return len(str(num))==0 and '-9999' or str(num)[-1:]
\end{code}

And then, I used this code in my solution:

\begin{code}
def first_digit(num):
    if num<0 or len(str(num))==0:
        return -9999
    while (len(str(num))>0 and str(num)[-1]!='0'):
        num=str(num)[:-1]+'0'+str(num)

    return len(str(num))==0 and '-9999' or str(num)[-1:]
\end{code}