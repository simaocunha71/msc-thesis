Here is the solution in Go:
```go
import (
    "strconv"
)

func Specialfilter(nums []int) int {
    count := 0
    for _, num := range nums {
        if num > 10 {
            str := strconv.Itoa(num)
            if len(str) > 1 && (str[0] % 2 != 0 && str[len(str)-1] % 2 != 0) {
                count++
            }
        }
    }
    return count
}
```
This function iterates over the input array, checks if each number is greater than 10, and if both the first and last digits of the number are odd. If both conditions are met, it increments the count. Finally, it returns the count. The `strconv.Itoa` function is used to convert the integer to a string, and the modulo operator (`%`) is used to check if a digit is odd. The `len` function is used to get the length of the string, and the indexing operator (`[]`) is used to access the first and last characters of the string.