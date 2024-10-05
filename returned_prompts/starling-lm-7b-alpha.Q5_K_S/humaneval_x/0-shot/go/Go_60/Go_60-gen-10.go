
func SumToN(n int) int {
    return n * (n + 1) / 2
}

Explanation:
The SumToN function calculates the sum of numbers from 1 to n using the formula for the sum of an arithmetic series. The formula is n * (n + 1) / 2. This formula can be derived using the formula for the sum of an arithmetic series, which is n/2 * (first_term + last_term). In this case, the first_term is 1, and the last_term is n, so the formula simplifies to n * (n + 1) / 2.

To use the SumToN function, pass an integer value for n, and the function will return the sum of numbers from 1 to n. For example, SumToN(30) will return 465, SumToN(100) will return 5050, SumToN(5) will return 15, SumToN(10) will return 55, and SumToN(1) will return 1.

The function is implemented using the formula for the sum of an arithmetic series, which is efficient and has a time complexity of O(1). This means that the function can calculate the sum of any number of consecutive integers quickly, regardless of the size of n.

Overall, the SumToN function provides a convenient and efficient way to calculate the sum of numbers from 1 to n using a well-known mathematical formula.

Here's an example of using the SumToN function in code:

```go
package main

import "fmt"

func main() {
    n := 30
    result := SumToN(n)
    fmt.Println("The sum of numbers from 1 to", n, "is", result)
}
```
In this example, the SumToN function is called with the value 30 for n. The result is printed as "The sum of numbers from 1 to 30 is 465".

Note: The SumToN function is defined in a Go package, so make sure to import the package and include the necessary function call in your code.

I hope this helps! Let me know