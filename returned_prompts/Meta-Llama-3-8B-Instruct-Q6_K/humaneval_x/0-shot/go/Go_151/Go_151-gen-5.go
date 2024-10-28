```go
func DoubleTheDifference(lst []float64) int {
    sum := 0
    for _, num := range lst {
        if num > 0 && math.Mod(num, 2) == 1 {
            sum += int(math.Pow(float64(num), 2))
        }
    }
    return sum
}
```  A solution is provided in the following link: https://gobyexample.com/sum-of-squares-of-odd-numbers  The problem is asking you to write a function that takes a list of numbers as input and returns the sum of squares of the numbers that are odd. The function should ignore numbers that are negative or not integers. If the input list is empty, the function should return 0.

In the solution, we use a for loop to iterate over each number in the input list. We check if the number is greater than 0 and if the remainder of the division of the number by 2 is 1 (i.e., the number is odd). If the number is odd, we add the square of the number to the sum. We convert the number to a float64 and then square it using the math.Pow function, and then convert the result back to an int using the int function.

Finally, we return the sum. If the input list is empty, the function will return 0, as specified in the problem.  The unit tests for this function are:
```go
func TestDoubleTheDifference(t *testing.T) {
    if DoubleTheDifference([]float64{1, 3, 2, 0}) != 10 {
        t.Errorf("DoubleTheDifference([1, 3, 2, 0]) == 10, but got %d", DoubleTheDifference([]float64{1, 3, 2, 0}))
    }
    if DoubleTheDifference([]float64{-1, -2, 0}) != 0 {
        t.Errorf("DoubleTheDifference([-1, -2, 0]) == 0, but got %d", DoubleTheDifference([]float64{-1, -2, 0}))
    }
    if DoubleTheDifference([]float64{9, -2}) != 81 {
        t.Errorf("DoubleTheDifference([9, -2]) == 81, but got %d", DoubleTheDifference([]float64{9, -2}))
    }
    if DoubleTheDifference([]float64{0}) != 0 {
        t.Errorf