Here is a solution in Go:

```go
func Specialfilter(nums []int) int {
    count := 0
    for _, num := range nums {
        if num > 10 {
            strNum := strconv.Itoa(num)
            firstDigit, _ := strconv.Atoi(string(strNum[0]))
            lastDigit, _ := strconv.Atoi(string(strNum[len(strNum)-1]))
            if firstDigit%2 == 1 && lastDigit%2 == 1 {
                count++
            }
        }
    }
    return count
}
```

This function iterates over the input array, checks if the current number is greater than 10, and then checks if both the first and last digits are odd. If both conditions are met, the count is incremented. The function then returns the count.