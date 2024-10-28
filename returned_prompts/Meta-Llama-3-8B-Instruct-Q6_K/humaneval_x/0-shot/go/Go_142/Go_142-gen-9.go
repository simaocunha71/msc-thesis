Here is the solution in Go:

```go
package main

import (
    "math"
)

func SumSquares(lst []int) int {
    var sum int
    for i, v := range lst {
        if i%3 == 0 && i%4 != 0 {
            sum += int(math.Pow(float64(v), 2))
        } else if i%4 == 0 && i%3 != 0 {
            sum += int(math.Pow(float64(v), 3))
        } else {
            sum += v
        }
    }
    return sum
}

func main() {
    lst := []int{1, 2, 3}
    result := SumSquares(lst)
    println(result)  // Output: 6
}
```

In this solution, we use a for loop to iterate over the list. We use the modulus operator to check if the index is a multiple of 3 or 4. If the index is a multiple of 3 and not 4, we square the value. If the index is a multiple of 4 and not 3, we cube the value. Otherwise, we just add the original value to the sum. We return the sum at the end. In the main function, we test this function with a list and print the result.