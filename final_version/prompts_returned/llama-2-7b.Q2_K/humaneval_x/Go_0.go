import (
    "math"
)

// Check if in given list of numbers, are any two numbers closer to each other than given threshold.
// >>> HasCloseElements([]float64{1.0, 2.0, 3.0}, 0.5)
// false
// >>> HasCloseElements([]float64{1.0, 2.8, 3.0, 4.0, 5.0, 2.0}, 0.3)
// true
func HasCloseElements(numbers []float64, threshold float64) bool {
    if len(numbers) < 2 {
        return false
    }

    for i := 0; i < len(numbers); i++ {
        for j, n := range numbers[1 : len(numbers)-1] {
            if distSquared(n, numbers[i]) >= threshold*threshold && !math.IsNaN(distSquared(n, numbers[i])) {
                return true
            }
        }
    }

    // Not found.
    return false
}