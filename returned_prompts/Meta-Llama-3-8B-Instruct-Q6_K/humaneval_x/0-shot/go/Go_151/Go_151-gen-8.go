```go
func DoubleTheDifference(lst []float64) int {
    var sum int
    for _, num := range lst {
        if math.Abs(num) % 1 == 0 && num > 0 {
            sum += int(math.Pow(float64(num), 2))
        }
    }
    return sum
}
```


Explanation:
The function takes a slice of float64 numbers as input and returns the sum of squares of the odd numbers in the list.
The function uses a for loop to iterate over each number in the list.
For each number, it checks if the absolute value of the number is an integer (using `math.Abs(num) % 1 == 0`) and if it is positive (using `num > 0`). If both conditions are true, it adds the square of the number to the sum.
The function returns the sum at the end.
The math.Pow function is used to calculate the square of a number.
The int function is used to convert the sum to an integer, as the sum is a float64 value.
The function returns 0 if the input list is empty.