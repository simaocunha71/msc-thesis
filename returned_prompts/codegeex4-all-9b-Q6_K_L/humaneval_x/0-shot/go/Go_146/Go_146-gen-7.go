Here is a solution written in Go:

```go
func Specialfilter(nums []int) int {
    count := 0
    for _, num := range nums {
        if num > 10 {
            strNum := strconv.Itoa(num)
            if strNum[0] % 2 == 1 && strNum[len(strNum)-1] % 2 == 1 {
                count++
            }
        }
    }
    return count
}
```

This function takes an array of numbers as input and returns the number of elements in the array that are greater than 10 and both first and last digits of a number are odd (1, 3, 5, 7, 9). It converts each number to a string and checks if the first and last characters of the string are odd. If they are, it increments the count. Finally, it returns the count.