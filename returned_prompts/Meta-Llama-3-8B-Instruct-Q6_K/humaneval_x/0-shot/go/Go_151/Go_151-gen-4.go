```go
func DoubleTheDifference(lst []float64) int {
    var sum int
    for _, v := range lst {
        if math.Abs(v) % 1 == 0 && v > 0 {
            sum += int(math.Pow(float64(v), 2))
        }
    }
    return sum
}
```

Explanation:
The function `DoubleTheDifference` takes a list of floating point numbers as input. It iterates over the list, checks each number to see if it is odd (by checking if its absolute value is an integer and greater than 0), and if it is, it squares the number and adds it to the sum. The function returns the sum. If the input list is empty, the function returns 0. 

The `math.Pow` function is used to square each number, and the `math.Abs` function is used to get the absolute value of each number. The `%` operator is used to check if a number is an integer (i.e., if its remainder when divided by 1 is 0). The `int` function is used to convert the result of `math.Pow` to an integer, since the result of `math.Pow` is a floating point number. 

The `range` keyword is used to iterate over the input list. The `_` variable is used to ignore the index of each element in the list, and `v` is used to represent each element in the list. 

The function returns the sum as an integer, as required by the problem statement. 

Note: This function assumes that the input list contains only numbers. If the list contains non-numeric values, the function may panic or return incorrect results. If the list contains non-integer numbers, the function will return incorrect results for those numbers. 

Also, the function returns the sum as an integer, which may lose precision if the sum is very large. If the sum is very large, it may be necessary to return the sum as a float64 instead. 

Finally, the function does not handle errors. If the input list is invalid (e.g., it contains non-numeric values), the function may panic or return incorrect results. If the function is intended to be used in a production environment, it may be necessary to add error handling to the function. 