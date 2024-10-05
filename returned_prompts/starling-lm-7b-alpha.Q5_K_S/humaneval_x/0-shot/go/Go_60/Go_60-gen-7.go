
To calculate the sum of numbers from 1 to n, we can use the following formula:

sum = (n * (n + 1)) / 2

The function SumToN takes an integer n as input and returns the sum as an integer. Here's how it works:

1. The function takes the input parameter n, which represents the upper limit of the sum.
2. It uses the formula mentioned above to calculate the sum by multiplying n with (n + 1) and dividing the result by 2.
3. The calculated sum is then returned as the result of the function.

For example, when SumToN(30) is called, it calculates the sum of numbers from 1 to 30, which is (30 * (30 + 1)) / 2 = 465. Similarly, SumToN(100) calculates the sum of numbers from 1 to 100, which is (100 * (100 + 1)) / 2 = 5050.

You can test the function with different values of n to see the corresponding sums.

Here's an example of how you can use the SumToN function in your code:

```go
package main

import "fmt"

func main() {
    n := 30
    result := SumToN(n)
    fmt.Println(result)
}
```

In this example, the main function calls the SumToN function with n set to 30. The returned sum is then printed to the console, which in this case is 465.

You can modify the value of n to calculate the sum for different ranges of numbers.

I hope this helps you understand how the SumToN function works and how to use it in your code! Let me know if you have any more questions.

```go
package main

import "fmt"

func SumToN(n int) int {
    return (n * (n + 1)) / 2
}
```

```

```

```go
package main

import "fmt"

func main() {
    n := 30
    result := SumToN