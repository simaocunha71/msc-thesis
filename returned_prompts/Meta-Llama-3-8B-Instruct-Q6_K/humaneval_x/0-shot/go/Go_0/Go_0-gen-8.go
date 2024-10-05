Here is the solution:

```go
import (
    "math"
)

func HasCloseElements(numbers []float64, threshold float64) bool {
    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            if math.Abs(numbers[i] - numbers[j]) < threshold {
                return true
            }
        }
    }
    return false
}
```

This function iterates over the list of numbers and checks if the absolute difference between any two numbers is less than the given threshold. If it finds such a pair, it returns `true`. If it checks all pairs and doesn't find any close elements, it returns `false`. 

You can test this function with the examples you provided:

```go
func main() {
    fmt.Println(HasCloseElements([]float64{1.0, 2.0, 3.0}, 0.5)) // false
    fmt.Println(HasCloseElements([]float64{1.0, 2.8, 3.0, 4.0, 5.0, 2.0}, 0.3)) // true
}
```

This will output:

```
false
true
```  which matches the expected results. 