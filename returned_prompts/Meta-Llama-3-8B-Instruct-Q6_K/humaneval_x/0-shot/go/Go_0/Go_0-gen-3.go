Here is a simple solution in Go:
```go
package main

import (
    "fmt"
    "math"
)

func HasCloseElements(numbers []float64, threshold float64) bool {
    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            if math.Abs(numbers[i]-numbers[j]) < threshold {
                return true
            }
        }
    }
    return false
}

func main() {
    fmt.Println(HasCloseElements([]float64{1.0, 2.0, 3.0}, 0.5))  // false
    fmt.Println(HasCloseElements([]float64{1.0, 2.8, 3.0, 4.0, 5.0, 2.0}, 0.3))  // true
}
```
This function iterates over the list of numbers and checks for each pair of numbers if the absolute difference is less than the given threshold. If it finds such a pair, it returns `true`. If it checks all pairs and doesn't find any, it returns `false`. 

The `math.Abs` function is used to calculate the absolute difference between two numbers. 

The `HasCloseElements` function is tested in the `main` function with two examples. The first example has no pairs of numbers that are closer than the threshold, so it returns `false`. The second example has pairs of numbers that are closer than the threshold, so it returns `true`. 

Please note that this function has a time complexity of O(n^2) where n is the length of the input slice. This is because it checks all pairs of numbers. If you need a more efficient solution, you could sort the input slice first and then check for close elements in a single pass, which would have a time complexity of O(n log n). 