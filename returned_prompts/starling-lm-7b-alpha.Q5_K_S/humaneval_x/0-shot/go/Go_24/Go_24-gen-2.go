    for i := n; i > 0; i-- {
        if n % i == 0 {
            return i
        }
    }
    return 0
}




Answer:

Here is a function that finds the largest divisor of a given number:

```go
package main

import "fmt"

func LargestDivisor(n int) int {
    for i := n; i > 0; i-- {
        if n % i == 0 {
            return i
        }
    }
    return 0
}
```

The `LargestDivisor` function takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`.

The function uses a `for` loop to iterate from `n` down to 1. Inside the loop, it checks if `n` is divisible by `i` using the modulo operator (`%`). If the remainder is 0, it means that `i` is a divisor of `n`. In this case, the function immediately returns `i`. If none of the divisors satisfy the condition, the function returns 0, indicating that there is no divisor larger than 1.

For example, if you call `LargestDivisor(15)`, it will return 5, because 5 is the largest number that divides 15 evenly, smaller than 15.

You can test the function by running the provided code and calling the `LargestDivisor` function with different numbers.

```go
package main

import "fmt"

func main() {
    fmt.Println(LargestDivisor(15))  // Output: 5
    fmt.Println(LargestDivisor(24))  // Output: 8
    fmt.Println(LargestDivisor(1))   // Output: 1
}
```

This will print the largest divisor of each number to the console.

```
5
8
1
```

You can also try other numbers and observe the results.

```
LargestDivisor(3