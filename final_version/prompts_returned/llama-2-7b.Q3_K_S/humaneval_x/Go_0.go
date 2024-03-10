import (
    "math"
)

// Check if in given list of numbers, are any two numbers closer to each other than given threshold.
// >>> HasCloseElements([]float64{1.0, 2.0, 3.0}, 0.5)
// false
// >>> HasCloseElements([]float64{1.0, 2.8, 3.0, 4.0, 5.0, 2.0}, 0.3)
// true
func HasCloseElements(numbers []float64, threshold float64) bool {
    if len(numbers) == 0 {
        return false
    }

    var i = 0
    for ; i < len(numbers); i++ { // Iterate through the entire list
        for j := 1; j <= i; j++ { // Loop to check all elements until current element.
            if numbers[i]-numbers[j] > threshold || (i+1 < len(numbers)) && numbers[i+1] - numbers[j] > threshold { // If not close to current element, or close to the next element, go ahead and break out of the loop.
                continue
            }
        }
    return true // Check if no other elements are closer than the ones we have already.
    }
}
