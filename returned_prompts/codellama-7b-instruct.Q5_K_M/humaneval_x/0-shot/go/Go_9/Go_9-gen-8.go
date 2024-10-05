import (
    "math"
)

// From a given list of integers, generate a list of rolling maximum element found until given moment
// in the sequence.
// >>> RollingMax([1, 2, 3, 2, 3, 4, 2])
// [1, 2, 3, 3, 3, 4, 4]
func RollingMax(numbers []int) []int {

func main() {
    numbers := []int{1, 2, 3, 2, 3, 4, 2}
    fmt.Println(RollingMax(numbers))
}
