Here is the solution to the problem:
```go
import (
    "strconv"
)

func AddElements(arr []int, k int) int {
    sum := 0
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
This function iterates over the first `k` elements of the array, converts each integer to a string, and checks if the length of the string is less than or equal to 2. If it is, it converts the string back to an integer and adds it to the sum. Finally, it returns the sum.

For example, if `arr = [111,21,3,4000,5,6,7,8,9]` and `k = 4`, the function will return `24` because the sum of the elements with at most two digits from the first 4 elements is `21 + 3 = 24`.