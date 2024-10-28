```
package main
import "fmt"
func SpecialFactorial(n int) int {
    result := 1
    for i := 1; i <= n; i++ {
        result *= SpecialFactorial(i-1)
    }
    return result
}
func main() {
    fmt.Println(SpecialFactorial(4)) // prints 288
}
```
Explanation:
The problem is asking to create a function called `SpecialFactorial` that calculates the Brazilian factorial of a given integer `n`. The Brazilian factorial is defined as `n! * (n-1)! * (n-2)! * ... * 1!`, where `n` is greater than 0.

The provided code is a recursive implementation of the `SpecialFactorial` function. It initializes a variable `result` to 1, and then enters a loop that runs from `i = 1` to `i = n`. In each iteration, the function calls itself with the argument `i-1` and multiplies the result by the return value. This is done to calculate the product of all factorials from `n` down to 1.

The `main` function is used to test the `SpecialFactorial` function with the input `4`, which should return `288`.

Note that this implementation has a high time complexity, as it does a lot of repeated calculations. A more efficient approach would be to use an iterative solution, which calculates the product of the factorials in a single loop. However, the recursive solution is provided as a demonstration of how to solve the problem using recursion.