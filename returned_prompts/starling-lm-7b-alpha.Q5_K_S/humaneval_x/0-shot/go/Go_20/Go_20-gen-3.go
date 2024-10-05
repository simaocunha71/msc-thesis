
func FindClosestElements(numbers []float64) (result [2]float64) {
    if len(numbers) < 2 {
        return result
    }
    min := math.Abs(numbers[0] - numbers[1])
    index1, index2 := 0, 1
    for i, v := range numbers {
        for j, w := range numbers {
            if i != j && math.Abs(v-w) < min {
                min = math.Abs(v-w)
                index1, index2 = i, j
            }
        }
    }
    result[0], result[1] = numbers[index1], numbers[index2]
    return result
}


Here's a Go function that finds the closest elements from a supplied list of numbers:

The `FindClosestElements` function takes a slice of float64 (numbers) as input and returns a slice of float64 (result) containing the two closest elements. If the length of the input slice is less than 2, it returns an empty result.

The function initializes `min` as the absolute difference between the first two elements in the input slice (`numbers[0]` and `numbers[1]`). It also initializes `index1` and `index2` as the indices of these two elements.

Then, it iterates over all pairs of elements in the input slice using nested loops. For each pair, it calculates the absolute difference between the elements (`math.Abs(v-w)`) and compares it with the current minimum (`min`). If the absolute difference is smaller than the current minimum, it updates `min` and `index1` and `index2` to the indices of the current pair.

Finally, it assigns the values of the closest elements (`numbers[index1]` and `numbers[index2]`) to the result slice (`result[0]` and `result[1]`).

The function returns the result slice containing the two closest elements.

Example usage:

`FindClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.