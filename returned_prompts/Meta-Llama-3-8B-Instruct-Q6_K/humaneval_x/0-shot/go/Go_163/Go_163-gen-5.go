```go
func GenerateIntegers(a, b int) []int {
    var result []int
    if a > b {
        a, b = b, a
    }
    for i := a; i <= b; i++ {
        for _, digit := range strconv.Itoa(i) {
            if digit == '0' || digit == '2' || digit == '4' || digit == '6' || digit == '8' {
                result = append(result, i)
                break
            }
        }
    }
    return result
}
```


The above code generates even digits between a and b. It first checks if a is greater than b and swaps them if necessary. Then it iterates over each number from a to b. For each number, it converts the number to a string and checks each digit. If the digit is even (0, 2, 4, 6, or 8), it appends the number to the result slice and breaks the inner loop to move on to the next number. Finally, it returns the result slice. The time complexity is O(b-a), and the space complexity is O(b-a) as well.