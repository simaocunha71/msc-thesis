```go
func EvenOddCount(num int) [2]int {
    evenCount := 0
    oddCount := 0
    for num != 0 {
        digit := num % 10
        if digit%2 == 0 {
            evenCount++
        } else {
            oddCount++
        }
        num = num / 10
    }
    return [2]int{evenCount, oddCount}
}
```


This function iterates over each digit of the input number, checks if it is even or odd, and increments the corresponding count. It uses integer division (`num = num / 10`) to remove the last digit from the number, and the modulus operator (`num % 10`) to get the last digit. The function returns a tuple (array of two integers) containing the counts of even and odd digits. The example function calls provided in the problem statement are used to test this function.