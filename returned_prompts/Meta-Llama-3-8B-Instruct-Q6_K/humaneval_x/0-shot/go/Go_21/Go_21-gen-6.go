```
func RescaleToUnit(numbers []float64) []float64 {
    if len(numbers) < 2 {
        return nil
    }
    min := math.MinFloat64
    max := math.MaxFloat64
    for _, num := range numbers {
        if num < min {
            min = num
        }
        if num > max {
            max = num
        }
    }
    if min == max {
        return numbers
    }
    return scale(numbers, min, max)
}

func scale(numbers []float64, min, max float64) []float64 {
    result := make([]float64, len(numbers))
    for i, num := range numbers {
        result[i] = (num - min) / (max - min)
    }
    return result
}
```


Explanation:

The `RescaleToUnit` function takes a list of numbers as input and returns a new list where the smallest number is 0 and the largest is 1. It first checks if the input list has at least two elements, if not, it returns `nil`. Then it finds the minimum and maximum values in the list.

If the minimum and maximum values are the same, the function returns the original list, as there is no need to rescale.

The `scale` function is used to rescale the list. It creates a new list and for each number in the original list, it calculates the new value by subtracting the minimum value from the number and then dividing by the difference between the maximum and minimum values. This ensures that the new values are in the range [0, 1]. The `scale` function is called from `RescaleToUnit` with the minimum and maximum values found earlier.

The time complexity of this solution is O(n), where n is the length of the input list, as it needs to iterate over the list twice: once to find the minimum and maximum values, and once to rescale the list. The space complexity is also O(n), as it needs to create a new list to store the rescaled values.