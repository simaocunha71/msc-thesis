```go
func Specialfilter(nums []int) int {
    count := 0
    for _, num := range nums {
        if num > 10 {
            str := strconv.Itoa(num)
            if len(str) > 1 && (int(str[0]-'0') % 2 != 0 && int(str[len(str)-1]-'0') % 2 != 0) {
                count++
            }
        }
    }
    return count
}
```


This function iterates through each number in the input array. For each number, it checks if the number is greater than 10. If it is, it converts the number to a string and checks if the first and last digits are odd. If they are, it increments the count. Finally, it returns the count.