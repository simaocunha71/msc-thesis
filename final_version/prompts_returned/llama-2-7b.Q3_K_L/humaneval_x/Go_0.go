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

    sum := 0.0

    for _, number := range numbers {
        sum += math.Abs((number - sum) / 10)
    }

    min := math.MaxFloat64
    max := math.MinFloat64
    for i, num := range numbers {
        if i > 0 {
            distance := math.Abs(numbers[i] - numbers[len(numbers)-1])
            if distance < threshold && min >= distance && distance > 0 {
                min = distance
            }
        } else if distance <= threshold {
            max = distance
        }
    }

    return math.Abs((min / sum) - threshold) * (max / sum) < 1.0
}
