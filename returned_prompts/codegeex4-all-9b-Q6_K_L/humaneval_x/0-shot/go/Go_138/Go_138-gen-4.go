func IsEqualToSumEven(n int) bool {
    // check if n is even
    if n % 2 != 0 {
        return false
    }
    // check if n is greater than or equal to 8
    if n < 8 {
        return false
    }
    // check if n is divisible by 4
    if n % 4 != 0 {
        return false
    }
    return true
}

Explanation:
The given number n can be written as the sum of exactly 4 positive even numbers if and only if n is even, greater than or equal to 8, and divisible by 4.

In the above code, we first check if n is even. If it is not, we return false. Then, we check if n is greater than or equal to 8. If it is not, we return false. Finally, we check if n is divisible by 4. If it is not, we return false. If all these conditions are satisfied, we return true.