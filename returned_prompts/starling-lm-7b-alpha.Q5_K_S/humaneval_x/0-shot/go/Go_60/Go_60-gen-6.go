SumToN := func(n int) int {
    // Implement the logic to sum numbers from 1 to n
    return (n * (n + 1)) / 2
}

return SumToN(n)
}

In this solution, the SumToN function is implemented using the formula for the sum of an arithmetic series, which is (n * (n + 1)) / 2. This formula allows us to calculate the sum of numbers from 1 to n efficiently. The function takes an integer parameter n and returns the sum as an integer.

The formula for the sum of an arithmetic series is derived from the concept of arithmetic progression. In an arithmetic progression, the difference between consecutive terms is constant. The formula for the sum of an arithmetic series is derived from the concept of arithmetic progression.

Here's how the formula works:

- (n * (n + 1)) / 2: This is the formula for the sum of an arithmetic series. It calculates the sum of the numbers from 1 to n. The expression (n * (n + 1)) gives us the product of n and n + 1, and dividing it by 2 gives us the sum.

- n: This represents the upper limit of the range of numbers we want to sum. In this case, it's the input parameter 'n'.

- n + 1: This is the last term of the range of numbers we want to sum. It's calculated by adding 1 to the upper limit 'n'.

By using this formula, we can efficiently calculate the sum of numbers from 1 to n. The SumToN function takes an integer parameter 'n' and returns the sum as an integer.

To test the function, you can use the provided test cases:

- SumToN(30): This should return 465, as the sum of numbers from 1 to 30 is 465.
- SumToN(100): This should return 5050, as the sum of numbers from 1 to 100 is 5050.
- SumToN(5): This should return 15, as the sum of numbers from 1 to 5 is 15.