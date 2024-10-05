Here is a Go solution for the problem:

```go
import (
    "strconv"
)

func AddElements(arr []int, k int) int {
    var sum int
    for i := 0; i < k; i++ {
        str := strconv.Itoa(arr[i])
        if len(str) <= 2 {
            num, _ := strconv.Atoi(str)
            sum += num
        }
    }
    return sum
}
```

This function iterates over the first k elements of the array, converts each element to a string, checks if the length of the string is less than or equal to 2 (i.e., if the number has at most 2 digits), and if so, adds it to the sum. The sum is then returned. The `_` symbol is used to ignore the error returned by `strconv.Atoi`, since we are not interested in it in this case. 

The time complexity of this solution is O(k), where k is the number of elements in the array, since we are iterating over the array once. The space complexity is O(1), since we are using a constant amount of space to store the sum. 

This solution assumes that the input array is non-empty and that k is within the valid range. It also assumes that the elements of the array are integers. If these assumptions are not valid, additional error checking code may be needed. 