```go
func CountNums(arr []int) int {
    count := 0
    for _, num := range arr {
        s := strconv.Itoa(abs(num))
        sum := 0
        for _, c := range s {
            sum += int(c - '0')
        }
        if sum > 0 {
            count++
        }
    }
    return count
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}
```


The `CountNums` function iterates over each number in the input array. For each number, it converts it to a string and calculates the sum of its digits using a nested loop. It uses the `abs` function to ensure that negative numbers are treated correctly. If the sum of the digits is greater than 0, it increments the `count` variable. Finally, it returns the total count of numbers with a sum of digits > 0.

The `abs` function is a simple helper function that returns the absolute value of its input. It is used to handle negative numbers correctly. For example, if the input number is -123, the `abs` function will return 123, which is then converted to a string and processed as usual. This ensures that negative numbers are treated the same as positive numbers for the purpose of calculating the sum of their digits.