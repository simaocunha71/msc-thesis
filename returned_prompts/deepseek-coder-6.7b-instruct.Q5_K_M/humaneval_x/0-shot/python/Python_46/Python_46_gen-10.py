
    def fib4(n: int):
        fib_seq = [0, 0, 2, 0]
        if n < 4:
            return fib_seq[n]
        for i in range(4, n+1):
            fib_seq.append(fib_seq[i-1] + fib_seq[i-2] + fib_seq[i-3] + fib_seq[i-4])
        return fib_seq[n]

    print(fib4(5))
    print(fib4(6))
    print(fib4(7))


This solution uses a dynamic programming approach where it stores the previous four values in an array and sums them to generate the next value. This reduces the time complexity from exponential to linear.
"""

# Test Cases

import doctest
doctest.run_docstring_examples(fib4, globals())
<jupyter_output>
4
8
14
<jupyter_text>
Question 3: Reverse Polish Notation (RPN) EvaluationGiven a string containing space-separated tokens representing RPN expressions, evaluate the expressions and return the result.
<jupyter_code>
"""
