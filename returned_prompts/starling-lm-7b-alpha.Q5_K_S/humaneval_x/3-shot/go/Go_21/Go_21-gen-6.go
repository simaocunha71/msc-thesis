    return func(numbers []float64) []float64 {
        min_element := math.Min(numbers...)
        max_element := math.Max(numbers...)
        return func(numbers []float64) []float64 {
            return func(numbers []float64) []float64 {
                for i := range numbers {
                    numbers[i] = (numbers[i] - min_element) / (max_element - min_element)
                }
                return numbers
            }(numbers)
        }(numbers)
    }(numbers)
}



