To solve this problem, you can follow these steps:

1. Define a helper function called isPrime that takes an integer as input and returns a boolean value indicating whether the input is a prime number or not. This function should check if the input number is divisible by any number between 2 and the square root of the input number (inclusive). If any of these numbers are factors of the input number, return false; otherwise, return true.

2. Define another helper function called sumDigits that takes an integer as input and returns the sum of its digits. This function can be implemented using a while loop that repeatedly divides the input number by 10 and adds the remainder to a running total until the number becomes zero.

3. Iterate through the input list and find the largest number that is also a prime number using the isPrime function. You can keep track of the largest prime number found so far and update it whenever a larger prime number is encountered.

4. Once the largest prime number is found, call the sumDigits function to calculate the sum of its digits and return the result.

Here's an example implementation of the solution in Go:

```go
package main

import (
    "math"
    "strconv"
)

func isPrime(num int) bool {
    if num <= 1 {
        return false
    }
    for i := 2; i <= int(math.Sqrt(float64(num)))+1; i++ {
        if num%i == 0 {
            return false
        }
    }
    return true
}

func sumDigits(num int) int {
    sum := 0
    for num > 0 {
        sum += num % 10
        num /= 10
    }
    return sum
}

func Skjkasdkd(lst []int) int {
    largestPrime := 0
    for _, num := range lst {
        if isPrime(num) && num > largestPrime {
            largestPrime = num
        }
    }
    return sumDigits(largestPrime)
}
```

In this implementation, the isPrime function checks if a number is divisible by any number between