    if n <= 1 {
        return n
    }
    a, b := 0, 1
    for i := 2; i <= n; i++ {
        a, b = b, a+b
    }
    return b
}

B:
    if n <= 1 {
        return n
    }
    if n == 2 {
        return 1
    }
    a, b := 1, 1
    for i := 3; i <= n; i++ {
        a, b = b, a+b
    }
    return b
}

C:
    if n <= 1 {
        return n
    }
    a, b := 0, 1
    for i := 2; i <= n; i++ {
        a, b = b, a+b
    }
    return b
}

D:
    if n <= 1 {
        return n
    }
    if n == 2 {
        return 1
    }
    a, b := 1, 1
    for i := 3; i <= n; i++ {
        a, b = b, a+b
    }
    return b
}

Which one is correct?

A) Correct
B) Incorrect
C) Correct
D) Incorrect

Answer: A) Correct

Explanation: The correct implementation of the Fibonacci sequence is provided in A. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. The function correctly calculates the n-th Fibonacci number by using a for loop to iterate from 2 to n, and updating the values of a and b accordingly. The function returns the value of b, which is the n-th Fibonacci number.

The other options are incorrect because they either do not correctly calculate the Fibonacci sequence (B and D) or do not handle the base cases correctly (C). Option B returns 1 for n=2, which is incorrect. Option D returns 1 for n=2, which is also incorrect. Option C does not handle the base cases correctly, as it returns 0 for n=1, which is incorrect. Therefore, option A is the correct implementation of the Fibonacci sequence.