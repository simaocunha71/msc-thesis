
To solve this kata, you need to understand the concept of modular arithmetic. The operation you need to perform is called exponentiation modulo p (or mod p for short). It's a way to compute large powers quickly, while making sure the result stays within a given range.

Here's a step-by-step guide to help you understand the code:

1. Initialize a variable `result` to 1. This variable will hold the final result.
2. Create a while loop that runs as long as `n` is greater than 0. This loop will be responsible for calculating the powers of 2.
3. Inside the loop, calculate the modulo of `result` and `p`. This will ensure that the result stays within the specified range.
4. Multiply `result` by 2 and update the value of `result` with the new value.
5. Subtract 1 from `n` to decrease the power by 1. This is necessary to make the loop run for the correct number of iterations.
6. After the loop finishes, return the final value of `result`.

The time complexity of this solution is O(log n) because the while loop runs n times, where n is the number of bits in the binary representation of `n`.

The space complexity is O(1) because the function only uses a fixed amount of space regardless of the input size.

Here's a sample usage of the function to help you understand how it works:

```go
package main

import "fmt"

func Modp(n int, p int) int {
    result := 1
    for n > 0 {
        result = (result * 2) % p
        n--
    }
    return result
}

func main() {
    fmt.Println(Modp(3, 5))  // Output: 3
    fmt.Println(Modp(1101, 101))  // Output: 2
    fmt.Println(Modp(0, 101))  // Output: 1
    fmt.Println(Modp(3, 11))  // Output: 8
    fmt.Println(Modp(100, 101))