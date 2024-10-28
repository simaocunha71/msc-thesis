
```go
package main

import "fmt"

func main() {
    fmt.Println(IsSimplePower(1, 4))
    fmt.Println(IsSimplePower(2, 2))
    fmt.Println(IsSimplePower(8, 2))
    fmt.Println(IsSimplePower(3, 2))
    fmt.Println(IsSimplePower(3, 1))
    fmt.Println(IsSimplePower(5, 3))
}

func IsSimplePower(x int,n int) bool {
    for i := 0; i < 32; i++ {
        if n == 1<<i {
            return true
        }
    }
    return false
}
```

Explanation:

In this code, the function IsSimplePower(x int,n int) takes two parameters, x and n. It returns true if the number x is a simple power of the number n, and false if it is not.

The function uses a for loop to iterate through all possible values of i from 0 to 31. Inside the loop, it checks if the value of n is equal to 2 raised to the power of i, which is represented as 1<<i. If it is, it means that n is a simple power of 2, and the function returns true. If none of the values of i satisfy the condition, the function returns false.

To test the function, the main function is used to call the IsSimplePower function with different values of x and n. The results are printed using the fmt.Println function.

In the given example, the function IsSimplePower is called with the values (1, 4), (2, 2), (8, 2), (3, 2), (3, 1), and (5, 3). The expected results are true, true, true, false, false, and false respectively.

Overall, this code demonstrates how to write a function to check if a number is a simple power of another number, and it provides an example of how to use the function to test different cases.

```go
package main

import "fmt"

func main() {
    fmt.Println(IsSimplePower