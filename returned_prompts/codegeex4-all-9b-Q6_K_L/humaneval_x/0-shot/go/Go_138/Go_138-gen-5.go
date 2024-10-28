func IsEqualToSumEven(n int) bool {
    if n == 8 {
        return true
    }
    if n < 8 || n%2 != 0 {
        return false
    }
    for i := 2; i <= n/2; i += 2 {
        if IsEqualToSumEven(n-i) {
            return true
        }
    }
    return false
}

Explanation:
The function IsEqualToSumEven checks whether the given number n can be written as the sum of exactly 4 positive even numbers. 

The function first checks if n is equal to 8. If it is, then it returns true because 8 can be written as the sum of exactly 4 positive even numbers (2 + 2 + 2 + 2).

Next, the function checks if n is less than 8 or if n is not divisible by 2. If either of these conditions is true, then the function returns false because a number less than 8 or an odd number cannot be written as the sum of exactly 4 positive even numbers.

Finally, the function uses a for loop to iterate through all possible values of i from 2 to n/2, with a step of 2. For each value of i, the function calls itself recursively with the argument n-i. If the recursive call returns true, then the function returns true because the given number can be written as the sum of exactly 4 positive even numbers.

If none of the conditions are met, then the function returns false because the given number cannot be written as the sum of exactly 4 positive even numbers.