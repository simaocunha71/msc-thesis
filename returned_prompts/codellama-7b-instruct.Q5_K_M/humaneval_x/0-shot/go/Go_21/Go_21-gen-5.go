
// Given a list of numbers (of at least two elements), apply a linear transform to that list,
// such that the smallest number will become 0 and the largest will become 1
// >>> RescaleToUnit([1.0, 2.0, 3.0, 4.0, 5.0])
// [0.0, 0.25, 0.5, 0.75, 1.0]
func RescaleToUnit(numbers []float64) []float64 {
    min := math.Inf(1)
    max := math.Inf(-1)
    for _, n := range numbers {
        if n < min {
            min = n
        }
        if n > max {
            max = n
        }
    }
    if min == max {
        // This is a degenerate case, where all numbers are the same
        // so we cannot rescale, but we still need to return an array
        // of length len(numbers)
        result := make([]float64, len(numbers))
        for i := range result {
            result[i] = 1
        }
        return result
    }
    result := make([]float64, len(numbers))
    for i, n := range numbers {
        result[i] = (n - min) / (max - min)
    }
    return result
}
