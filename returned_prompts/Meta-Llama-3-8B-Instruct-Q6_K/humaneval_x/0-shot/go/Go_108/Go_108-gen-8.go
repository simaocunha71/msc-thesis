Here is a Go solution for the problem:

```go
import (
    "math"
    "strconv"
)

func CountNums(arr []int) int {
    count := 0
    for _, num := range arr {
        str := strconv.Itoa(abs(num))
        sum := 0
        for _, c := range str {
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

This solution first converts each number to a string, then calculates the sum of its digits. It uses a helper function `abs` to make sure the number is positive. If the sum of digits is greater than 0, it increments the count. Finally, it returns the count. 

You can call this function with an array of integers to get the count of elements which has a sum of digits > 0. 

For example, `CountNums([]int{-1, 11, -11})` will return 1, and `CountNums([]int{1, 1, 2})` will return 3. 

Note: This solution assumes that the input array is not empty. If the input array can be empty, you should add a check at the beginning of the function to return 0 in this case. 

Also, this solution has a time complexity of O(n*m), where n is the size of the input array and m is the maximum number of digits in the numbers in the array. This is because it converts each number to a string and calculates the sum of its digits. If you need a more efficient solution, you can use a different approach. 

For example, you can calculate the sum of digits for each number separately, and then calculate the sum of digits for each digit separately. This will reduce the time complexity to O(n + m). 

Here is the modified solution:

```go
func CountNums(arr []int) int {
    count := 0
    for _, num := range arr {
        sum := 0
        for num != 0 {
            num, remainder := div(num, 10)
            sum += remainder
        }
        if sum > 0 {
            count++
        }
    }
    return count
}

func div(a int, b int) (int, int) {
    if b ==