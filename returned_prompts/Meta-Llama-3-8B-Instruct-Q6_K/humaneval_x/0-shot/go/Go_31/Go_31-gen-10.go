```go
package main

import "fmt"

func IsPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i * i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}

func main() {
    fmt.Println(IsPrime(6))  // false
    fmt.Println(IsPrime(101))  // true
    fmt.Println(IsPrime(11))  // true
    fmt.Println(IsPrime(13441))  // true
    fmt.Println(IsPrime(61))  // true
    fmt.Println(IsPrime(4))  // false
    fmt.Println(IsPrime(1))  // false
}
```

Explanation:
The function `IsPrime(n int) bool` checks whether a given integer `n` is prime or not. 

A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

The function first checks if `n` is less than or equal to 1. If it is, the function returns `false`, because prime numbers are greater than 1.

Then, the function iterates from 2 to the square root of `n`. For each number `i` in this range, it checks if `n` is divisible by `i`. If `n` is divisible by `i`, the function returns `false`, because `n` is not prime.

If the function has not returned `false` after checking all the numbers in the range, it returns `true`, because `n` is prime.

The `main` function tests the `IsPrime` function with different inputs and prints the results. 

The output of the program will be:
```
false
true
true
true
true
false
false
```
This matches the expected results. For example, 6 is not prime because it can be divided by 2 and 3, but 101 is prime because it can only be divided by 1 and itself. Similarly, 4 is not prime because it can be divided by 2, but 13441 is prime because it can only be divided by 1 and itself. 

The time complexity of this function is O(sqrt(n)), which is quite efficient for large numbers. The space complexity is O(1), which means the function uses a constant amount of space, regardless of the size of the input. 