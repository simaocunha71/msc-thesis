To solve this problem, you need to follow these steps:

1. Find the largest prime number in the list.
2. Convert the largest prime number to a string.
3. Sum the digits of the largest prime number.
4. Return the sum.

Here's a step-by-step explanation of the solution:

1. Initialize a variable max to 0 and a variable prime to -1.
2. Iterate through the list using a for loop and check if each number is prime using a while loop. If a number is prime, compare it with the current max value. If the current number is greater than the current max value, update the max and prime variables.
3. After iterating through the entire list, convert the prime variable (which holds the largest prime number) to a string using the strconv.Itoa() function.
4. Initialize a variable sum to 0.
5. Iterate through each character of the prime string using a for loop and add each digit to the sum variable. Finally, return the sum.

Here's the code for the solution:

```go
package main

import (
    "math"
    "strconv"
)

func Skjkasdkd(lst []int) int {
    max := 0
    prime := -1

    for _, num := range lst {
        if isPrime(num) {
            if num > max {
                max = num
                prime = num
            }
        }
    }

    sum := 0
    str := strconv.Itoa(prime)

    for _, char := range str {
        sum += int(char - '0')
    }

    return sum
}

func isPrime(num int) bool {
    if num <= 1 {
        return false
    }

    for i := 2; i <= int(math.Sqrt(float64(num))); i++ {
        if num%i == 0 {
            return false
        }
    }

    return true
}
```

To test the code with different inputs, you can use the following test cases:

```go
func main() {
    testCases := []struct