
func RescaleToUnit(numbers []float64) []float64 {
    min, max := math.Min(numbers...), math.Max(numbers...)
    return scale(numbers, 0, 1, min, max)
}

func scale(numbers []float64, lo, hi, min, max float64) []float64 {
    for i := range numbers {
        numbers[i] = scale(numbers[i], lo, hi, min, max)
    }
    return numbers
}

func scale(x, lo, hi, min, max float64) float64 {
    return (x - min) / (max - min) * (hi - lo) + lo
}

To rescale a slice of numbers to the unit interval [0,1] in Go, you can define a function RescaleToUnit that takes the slice of numbers as input and returns the rescaled slice. The function uses another helper function scale to perform the rescaling. The scale function takes a number, the lower and upper bounds of the new interval, and the original minimum and maximum values, and returns the rescaled number. It does this by subtracting the original minimum from the number and dividing by the difference between the original maximum and minimum values. This gives a value between 0 and 1. It then multiplies this value by the difference between the upper and lower bounds of the new interval, and adds the lower bound value. This gives a number between the lower and upper bounds of the new interval.

The RescaleToUnit function first finds the minimum and maximum values in the input slice using the math.Min and math.Max functions respectively. It then calls the scale function on each number in the input slice, updating the number in place, and returns the rescaled slice.

In this way, the function RescaleToUnit can be used to rescale a slice of numbers to the unit interval [0,1] in Go.

// RescaleToUnit([1.0, 2.0, 3.0, 4.0, 5.0]) => [0.0, 0.25, 0.5, 0.75, 1.0]

Here is an example of how