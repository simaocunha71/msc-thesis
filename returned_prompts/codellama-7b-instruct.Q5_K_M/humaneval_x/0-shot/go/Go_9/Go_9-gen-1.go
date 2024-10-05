
import (
    "math"
)

// From a given list of integers, generate a list of rolling maximum element found until given moment
// in the sequence.
// >>> RollingMax([1, 2, 3, 2, 3, 4, 2])
// [1, 2, 3, 3, 3, 4, 4]
func RollingMax(numbers []int) []int {

    // Calculate the max of the first element
    max := math.MinInt64
    for _, i := range numbers {
        if i > max {
            max = i
        }
    }

    // Init the result list with the first max element
    result := make([]int, len(numbers))
    for i := range result {
        result[i] = max
    }

    // For each element of the list, find the maximum element before it and use it as the new max
    for i := 1; i < len(numbers); i++ {
        if numbers[i] > result[i-1] {
            result[i] = numbers[i]
        }
    }

    return result
}
