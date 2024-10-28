Here is a possible implementation of the `HasCloseElements` function in Go:
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
This function iterates over the list of numbers and checks if any two numbers are closer to each other than the given threshold. If it finds such a pair, it returns `true`. If it doesn't find any such pair after checking all pairs of numbers, it returns `false`.

You can test this function with the examples you provided:
```go
func main() {
    numbers1 := []float64{1.0, 2.0, 3.0}
    fmt.Println(HasCloseElements(numbers1, 0.5)) // false

    numbers2 := []float64{1.0, 2.8, 3.0, 4.0, 5.0, 2.0}
    fmt.Println(HasCloseElements(numbers2, 0.3)) // true
}
```
I hope this helps! Let me know if you have any questions.