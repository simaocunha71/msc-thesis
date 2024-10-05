You can solve this problem by iterating over the array of numbers and checking if each number satisfies the given conditions. Here's the implementation of the Specialfilter function:

```go
func Specialfilter(nums []int) int {
    count := 0

    for _, num := range nums {
        if num > 10 && isOdd(num) && isFirstAndLastDigitOdd(num) {
            count++
        }
    }

    return count
}

func isOdd(num int) bool {
    return num%2 != 0
}

func isFirstAndLastDigitOdd(num int) bool {
    str := strconv.Itoa(num)
    firstDigit := str[0] - '0'
    lastDigit := str[len(str)-1] - '0'

    return isOdd(firstDigit) && isOdd(lastDigit)
}
```

In this code, the Specialfilter function iterates over the array of numbers and checks if each number is greater than 10, both its first and last digits are odd. If a number satisfies these conditions, the count is incremented. Finally, the function returns the count.

The isOdd function checks if a number is odd by checking if the remainder of the number divided by 2 is not equal to 0.

The isFirstAndLastDigitOdd function converts the number to a string, extracts the first and last digits, and checks if both digits are odd using the isOdd function.