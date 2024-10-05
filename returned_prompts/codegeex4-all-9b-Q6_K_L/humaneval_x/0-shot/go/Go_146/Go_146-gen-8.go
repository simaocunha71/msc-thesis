Here is a Go solution for your problem. 

```go
func Specialfilter(nums []int) int {
    count := 0
    for _, num := range nums {
        if num > 10 && isOdd(num) {
            first, last := num%10, num/10000000
            if isOdd(first) && isOdd(last) {
                count++
            }
        }
    }
    return count
}

func isOdd(n int) bool {
    return n%2 != 0
}
```

The `Specialfilter` function loops through each number in the input array. It checks if the number is greater than 10 and if the first digit is odd by using the `isOdd` function. If both conditions are true, it checks if the last digit is odd by dividing the number by 10,000,000 (which gives the last digit) and checking if it's odd. If both the first and last digits are odd, it increments the count. Finally, it returns the count.

The `isOdd` function checks if a number is odd by checking if the remainder of the number divided by 2 is not equal to 0. If the remainder is not equal to 0, the number is odd and the function returns true. Otherwise, it returns false.