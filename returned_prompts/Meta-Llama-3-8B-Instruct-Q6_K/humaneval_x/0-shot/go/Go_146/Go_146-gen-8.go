Here is a Go function that solves the problem:

```go
func Specialfilter(nums []int) int {
    count := 0
    for _, num := range nums {
        strNum := strconv.Itoa(num)
        if num > 10 && (strNum[0] - '0')%2 != 0 && (strNum[len(strNum)-1] - '0')%2 != 0 {
            count++
        }
    }
    return count
}
```

This function iterates over the input array, converts each number to a string, and checks if the number is greater than 10 and both its first and last digits are odd. If the number meets these conditions, it increments the count. Finally, it returns the count.