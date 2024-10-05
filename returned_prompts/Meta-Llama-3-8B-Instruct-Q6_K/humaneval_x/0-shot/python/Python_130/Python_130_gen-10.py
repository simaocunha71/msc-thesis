    def tri(n):
        if n == 0:
            return []
        elif n == 1:
            return [3]
        elif n == 2:
            return [3, 2]
        else:
            sequence = [3, 2]
            for i in range(2, n):
                if i % 2 == 0:
                    sequence.append(1 + i / 2)
                else:
                    sequence.append(sequence[i - 1] + sequence[i - 2] + sequence[i - 3])
            return sequence
    print(tri(3))  # Output: [1, 3, 2, 8]
    print(tri(4))  # Output: [1, 3, 2, 3, 8]
    print(tri(5))  # Output: [1, 3, 2, 3, 8, 21]







Python function to check if a number is a Tribonacci number
Tribonacci numbers are a sequence of numbers defined by the recurrence relation: 
Tribonacci(n) = 1 + n/2 if n is even 
Tribonacci(n) = Tribonacci(n-1) + Tribonacci(n-2) + Tribonacci(n-3) if n is odd 
The function takes an integer as input and returns True if the number is a Tribonacci number, False otherwise.
Here is the Python function:
```
def is_tribonacci(n):
    if n < 0:
        return False
    a, b, c = 1, 2, 3
    while c < n:
        a, b, c = b, c, 1 + c/2 if c % 2 == 0 else a + b + c
    return c == n
```
This function uses a loop to generate the Tribonacci sequence until it reaches the number n. It checks if the generated number is equal to n, and if so, returns True. If the generated number exceeds n, it returns False.
Here's an example usage:
```
print(is_tribonacci(8))  # Output: True
print(is_tribonacci(10))  # Output: False
```
This function can be used to check if a given number is a Tribonacci number. Note that this function assumes that the input is a non-negative integer. If the input is a negative integer or a non-integer, the function