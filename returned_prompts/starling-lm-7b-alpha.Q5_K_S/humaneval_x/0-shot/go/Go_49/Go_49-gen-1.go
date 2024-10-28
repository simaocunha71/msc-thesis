To solve this problem, you can use the following steps:

1. Define a function named Modp that takes two integer parameters, n and p. This function will calculate the result of 2^n modulo p and return the result.

2. Inside the Modp function, you can use the exponentiation by squaring algorithm to efficiently calculate 2^n modulo p. This algorithm repeatedly squares the result and multiplies it by the original number. Here's a step-by-step breakdown of the algorithm:

   a. Set the result to 1.
   b. While n is greater than 0:
      i. If n is odd, multiply the result by 2 and then reduce it modulo p.
      ii. Divide n by 2 and reduce the result modulo p.

3. Outside the function, you can test the Modp function with different inputs to verify its correctness. Here are some example test cases:

   >>> Modp(3, 5)  # expected output: 3
   >>> Modp(1101, 101)  # expected output: 2
   >>> Modp(0, 101)  # expected output: 1
   >>> Modp(3, 11)  # expected output: 8
   >>> Modp(100, 101)  # expected output: 1

By following these steps and using the provided code, you can implement the Modp function that calculates 2^n modulo p efficiently and accurately.

Here's the code for the Modp function:

```go
package main

import "fmt"

func Modp(n int, p int) int {
    result := 1
    while n > 0 {
        if n%2 != 0 {
            result = (result * 2) % p
        }
        n /= 2
        result = result % p
    }
    return result
}

func main() {
    fmt.Println(Modp(3, 5))  // 3
    fmt.Println(Modp(1101, 101))  // 2
    fmt.Println(Modp(0, 10