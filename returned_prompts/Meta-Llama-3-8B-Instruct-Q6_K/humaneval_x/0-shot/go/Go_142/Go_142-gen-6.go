```go
import (
    "math"
)

func SumSquares(lst []int) int {
    var sum int
    for i, v := range lst {
        if i%3 == 0 {
            sum += int(math.Pow(float64(v), 2))
        } else if i%4 == 0 && i%3 != 0 {
            sum += int(math.Pow(float64(v), 3))
        } else {
            sum += v
        }
    }
    return sum
}
```


This function uses a for loop to iterate over the input list. It uses the range keyword to get both the index and value of each element. 
The if-else statement checks if the index is a multiple of 3, 4, or neither. If the index is a multiple of 3, it squares the value and adds it to the sum. 
If the index is a multiple of 4 but not 3, it cubes the value and adds it to the sum. If the index is neither a multiple of 3 nor 4, it adds the original value to the sum. 
Finally, the function returns the total sum. 

Note: The `math.Pow` function is used to calculate the square and cube of the values. The `int` function is used to convert the result back to an integer. 

The unit tests you provided can be used to verify the correctness of this function. For example, the test `SumSquares([]int{1,2,3})` should return `6`. 

The time complexity of this function is O(n), where n is the length of the input list. The space complexity is O(1) as it uses a constant amount of space. 














