import (
    "math"
)

// From a given list of integers, generate a list of rolling maximum element found until given moment
// in the sequence.
// >>> RollingMax([1, 2, 3, 2, 3, 4, 2])
// [1, 2, 3, 3, 3, 4, 4]
func RollingMax(numbers []int) []int {

    // Initialize the output array
    output := make([]int, len(numbers))

    // Initialize the maximum element
    max := math.MinInt

    // Iterate over the input array
    for i := 0; i < len(numbers); i++ {

        // If the current element is greater than the current maximum,
        // then update the maximum element
        if numbers[i] > max {
            max = numbers[i]
        }

        // Set the output element to the maximum element
        output[i] = max
    }

    // Return the output array
    return output
}



B:
import (
    "fmt"
    "math"
)

// From a given list of integers, generate a list of rolling maximum element found until given moment
// in the sequence.
// >>> RollingMax([1, 2, 3, 2, 3, 4, 2])
// [1, 2, 3, 3, 3, 4, 4]
func RollingMax(numbers []int) []int {

    // Initialize the output array
    output := make([]int, len(numbers))

    // Initialize the maximum element
    max := math.MinInt

    // Iterate over the input array
    for i := 0; i < len(numbers); i++ {

        // If the current element is greater than the current maximum,
        // then update the maximum element
        if numbers[i] > max {
            max = numbers[i]
        }

        // Set the output element to the maximum element
        output[i] = max
    }

    // Return the output array
    return output
}

func main() {

    // Declare