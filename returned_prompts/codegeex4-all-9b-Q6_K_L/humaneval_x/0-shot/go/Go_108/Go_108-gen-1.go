Here is the solution:

```go
func CountNums(arr []int) int {
    count := 0
    for _, num := range arr {
        if sumDigits(num) > 0 {
            count++
        }
    }
    return count
}

func sumDigits(n int) int {
    sum := 0
    sign := 1
    if n < 0 {
        sign = -1
        n = -n
    }
    for n > 0 {
        sum += n % 10
        n = n / 10
    }
    return sum * sign
}
```

In this code, the `CountNums` function iterates over each number in the array and checks if the sum of its digits is greater than 0. If it is, it increments the count. The `sumDigits` function calculates the sum of the digits of a number. It first checks if the number is negative and if so, takes the absolute value and sets the sign to -1. Then it iterates over each digit of the number, adding it to the sum, and dividing the number by 10 to remove the last digit. Finally, it returns the sum multiplied by the sign to handle negative numbers.