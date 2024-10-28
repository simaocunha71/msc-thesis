Here is the solution in Go:

```go
func FindClosestElements(numbers []float64) [2]float64 {
    if len(numbers) < 2 {
        return [2]float64{0, 0} // return two zeros if the list has less than two numbers
    }

    var closest [2]float64
    minDiff := float64(1<<63 - 1) // initialize the minimum difference to the maximum possible value

    for i := 0; i < len(numbers)-1; i++ {
        for j := i + 1; j < len(numbers); j++ {
            diff := math.Abs(numbers[i] - numbers[j])
            if diff < minDiff {
                minDiff = diff
                closest[0] = numbers[i]
                closest[1] = numbers[j]
            }
        }
    }

    return closest
}
```
The function `FindClosestElements` takes in a slice of float64 numbers and returns a two-element array containing the two numbers that are closest to each other. 

It first checks if the length of the list is less than two, and if so, it returns a two-element array of zeros. 

Then, it initializes an array `closest` to store the two closest numbers and a variable `minDiff` to store the minimum difference between any two numbers. 

It then iterates through all possible pairs of numbers in the list and calculates the absolute difference between each pair. If the difference is smaller than the current minimum difference, it updates the minimum difference and the `closest` array. 

Finally, it returns the `closest` array.