To solve this problem, we first need to round each element in the list to the upper int(Ceiling) first. Then, we can square each element and sum them up. Here's how you can implement this in Go:

```go
import (
    "math"
)

func SumSquares(lst []float64) int {
    sum := 0
    for _, num := range lst {
        // Round the number to the upper int(Ceiling)
        rounded := math.Ceil(num)
        // Square the rounded number and add to sum
        sum += int(rounded * rounded)
    }
    return sum
}
```

Now, let's test the function with the given examples:

```go
func main() {
    fmt.Println(SumSquares([]float64{1, 2, 3}))    // Output: 14
    fmt.Println(SumSquares([]float64{1, 4, 9}))    // Output: 98
    fmt.Println(SumSquares([]float64{1, 3, 5, 7}))  // Output: 84
    fmt.Println(SumSquares([]float64{1.4, 4.2, 0})) // Output: 29
    fmt.Println(SumSquares([]float64{-2.4, 1, 1}))  // Output: 6
}
```

This should give us the expected outputs.