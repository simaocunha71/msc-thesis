
To calculate the sum of the first n natural numbers, you can use the following formula: Sum = n * (n + 1) / 2.

In the SumToN function, you can implement this formula to calculate the sum of the first n natural numbers. Here's the updated function:

```go
package main

import "fmt"

func SumToN(n int) int {
    return n * (n + 1) / 2
}
```

To verify the accuracy of the SumToN function, you can use the provided test cases. Here's an example of how you can test the function:

```go
package main

import "fmt"

func main() {
    fmt.Println(SumToN(30))  // Output: 465
    fmt.Println(SumToN(100)) // Output: 5050
    fmt.Println(SumToN(5))   // Output: 15
    fmt.Println(SumToN(10))  // Output: 55
    fmt.Println(SumToN(1))   // Output: 1
}
```

When you run this code, you should see the expected output for each test case, indicating that the SumToN function is correctly calculating the sum of the first n natural numbers.

```
465
5050
15
55
1
```

By using the formula Sum = n * (n + 1) / 2, the SumToN function efficiently computes the sum of the first n natural numbers without the need for a loop or recursion.

```go
package main

import "fmt"

func SumToN(n int) int {
    return n * (n + 1) / 2
}
```

```go
package main

import "fmt"

func main() {
    fmt.Println(SumToN(30))  // Output: 465
    fmt.Println(SumToN(100)) // Output: 5050
    fmt.Println(SumToN(5))   // Output: 1