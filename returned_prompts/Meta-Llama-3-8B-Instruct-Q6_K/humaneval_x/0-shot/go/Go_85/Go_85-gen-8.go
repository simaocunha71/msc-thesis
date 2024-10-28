```go
package main

import "fmt"

func Add(lst []int) int {
    var sum int
    for i, v := range lst {
        if i%2 != 0 && v%2 == 0 {
            sum += v
        }
    }
    return sum
}

func main() {
    fmt.Println(Add([]int{4, 2, 6, 7})) // Output: 2
}
```

Explanation:

*   We use a for loop with a range variable `i` and `v` to iterate over the elements of the input list `lst`.
*   Inside the loop, we check if the index `i` is odd (`i % 2 != 0`) and the value `v` is even (`v % 2 == 0`).
*   If both conditions are true, we add the value `v` to the `sum` variable.
*   Finally, we return the `sum` variable as the result.
*   In the `main` function, we test the `Add` function with the input `[4, 2, 6, 7]` and print the output, which is `2`.