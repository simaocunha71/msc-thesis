Here is the solution in Go:
```go
func Specialfilter(nums []int) int {
    count := 0
    for _, num := range nums {
        if num > 10 {
            str := strconv.Itoa(num)
            firstDigit := int(str[0] - '0')
            lastDigit := int(str[len(str)-1] - '0')
            if firstDigit%2 != 0 && lastDigit%2 != 0 {
                count++
            }
        }
    }
    return count
}
```
This function iterates over each number in the input array. If the number is greater than 10, it converts the number to a string to extract the first and last digits. It then checks if both digits are odd by using the modulus operator (`%`). If both digits are odd, it increments the count. Finally, it returns the count of numbers that meet the conditions.