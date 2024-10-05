To solve this problem, you need to follow these steps:

1. Initialize a variable to store the maximum prime number found. Let's call it maxPrime. Set its initial value to 0.

2. Iterate through each number in the input list. For each number, check if it's a prime number.

3. To determine if a number is prime, you can follow these steps:

   a. Check if the number is less than or equal to 1. If it is, it's not a prime number. Move on to the next number in the list.

   b. Check if the number is a perfect square. If it is, it's not a prime number. Move on to the next number in the list.

   c. Check if the number is divisible by any number from 2 to the square root of the number. If it is, it's not a prime number. Move on to the next number in the list.

   d. If the number passes all the checks in steps a, b, and c, it's a prime number. Update the maxPrime variable with the current number if it's greater than the current maxPrime value.

4. After iterating through all the numbers in the input list, calculate the sum of the digits of the maxPrime variable. You can do this by converting the maxPrime variable to a string, iterating through each character in the string, converting each character to an integer, and adding them up.

5. Return the sum of the digits of the maxPrime variable as the result.

Here's an example implementation of the solution in Go:

```go
package main

import (
    "math"
    "strconv"
)

func Skjkasdkd(lst []int) int {
    maxPrime := 0

    for _, num := range lst {
        if num <= 1 {
            continue
        }
        if num == int(math.Pow(num, 0.5))*int(math.Pow(num, 0.5)) {
            continue
        }
        for i := 2; i <= int(math.Sqrt(float64(num))); i++ {
            if num