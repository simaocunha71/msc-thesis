
def histogram(test):
    d = {}
    if not test:
        return d
    else:
        words = test.split(' ')
        for word in words:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
        max_val = max(d.values())
        return {k: v for k, v in d.items() if v == max_val}

print(histogram('a b c'))
print(histogram('a b b a'))
print(histogram('a b c a b'))
print(histogram('b b b b a'))
print(histogram(''))


This solution will count the occurrence of each word in the input string and then return a dictionary containing only the words that have the maximum occurrence. In the case of several words having the maximum occurrence, all of them will be returned. If the input string is empty, an empty dictionary is returned.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2: Fibonacci Sequence Write a Python function that generates the nth Fibonacci number. The Fibonacci sequence is a sequence of numbers where each number is the sum of the two preceding ones. The sequence starts with 0 and 1.In mathematics, the sequence is defined by recurrence relation: F(n) = F(n-1) + F(n-2) with initial conditions F(0) = 0 and F(1) = 1.
<jupyter_code>
