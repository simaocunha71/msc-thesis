
SumToN(30) // 465
SumToN(100) // 5050
SumToN(5) // 15
SumToN(10) // 55
SumToN(1) // 1

In this code, the SumToN function takes an integer as an argument and returns an integer. The function calculates the sum of all the numbers from 1 to n using a mathematical formula.

The formula used is (n * (n + 1)) / 2, which is derived from the arithmetic series sum formula. This formula allows us to calculate the sum of an arithmetic series without having to add up each individual number.

For example, if we call SumToN(30), the function will calculate the sum of all the numbers from 1 to 30 using the formula and return the result, which is 465. Similarly, SumToN(100) will return 5050, SumToN(5) will return 15, SumToN(10) will return 55, and SumToN(1) will return 1.

The function is implemented in a straightforward manner, with the formula directly applied to calculate the sum. The result is then returned as the output of the function.

In summary, the SumToN function is a useful tool for quickly calculating the sum of numbers from 1 to n, without the need for manual addition.

// SumToN is a function that sums numbers from 1 to n.
// >>> SumToN(30)
// 465
// >>> SumToN(100)
// 5050
// >>> SumToN(5)
// 15
// >>> SumToN(10)
// 55
// >>> SumToN(1)
// 1
func SumToN(n int) int {
    return (n * (n + 1)) / 2
}

This code defines a function called SumToN that takes an integer as an argument and returns an integer. The function calculates the sum of all the numbers from 1 to n using a mathematical formula.

The formula used is (n * (n + 1)) / 2,