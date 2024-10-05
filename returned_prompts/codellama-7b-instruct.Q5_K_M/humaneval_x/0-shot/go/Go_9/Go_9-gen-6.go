
  for i in numbers:
    if i > max(numbers):
      numbers.append(i)
      numbers.append(max(numbers))
    else:
      numbers.append(max(numbers))
    return numbers
\end{code}

Answer: You can use the following code.

\begin{code}
def RollingMax(numbers):
    max_list = []
    for i in range(len(numbers)):
        temp_list = numbers[:i+1]
        max_list.append(max(temp_list))
    return max_list
\end{code}

This is the output of this code.

\begin{code}
>>> RollingMax([1, 2, 3, 2, 3, 4, 2])
[1, 2, 3, 3, 3, 4, 4]
\end{code}