The problem can be solved by checking if the given number is divisible by 4 and if not, then checking if it can be written as the sum of three even numbers. If the above conditions are not met, the function will return false.

Here is the code for the problem:

```go
func IsEqualToSumEven(n int) bool {
    if n % 4 == 0 {
        return true
    }
    for i := 2; i <= n/2; i += 2 {
        if n - i % 2 == 0 {
            return true
        }
    }
    return false
}
```

In the code above, we first check if the number is divisible by 4. If it is, we return true as it can be written as the sum of four even numbers (n/2, n/2, n/2, n/2).

If the number is not divisible by 4, we then check if it can be written as the sum of three even numbers. We iterate from 2 to n/2 (as the maximum possible even number that can be added is n/2) and for each even number, we check if the remaining number (n - i) is also even. If it is, we return true as it can be written as the sum of three even numbers (i, i, n - i).

If none of the above conditions are met, we return false as the number cannot be written as the sum of four positive even numbers.