```go
package main

import (
    "math"
    "strconv"
)

func CountNums(arr []int) int {
    count := 0
    for _, num := range arr {
        if num < 0 {
            num = -num
        }
        sum := 0
        for true {
            digit, err := strconv.Atoi(string(rune(num % 10)))
            if err != nil {
                break
            }
            sum += digit
            num /= 10
            if num == 0 {
                break
            }
        }
        if sum > 0 {
            count++
        }
    }
    return count
}

func main() {
    println(CountNums([]int{})) // 0
    println(CountNums([]int{-1, 11, -11})) // 1
    println(CountNums([]int{1, 1, 2})) // 3
}
```
Explanation:
The function `CountNums` iterates over each number in the input array. For each number, it calculates the sum of its digits. If the number is negative, it converts it to positive before calculating the sum. The sum of digits is calculated by repeatedly taking the last digit of the number using the modulus operator (`%`), converting it to an integer using `strconv.Atoi`, adding it to the sum, and then dividing the number by 10 to move to the next digit. This process continues until the number becomes 0. If the sum of digits is greater than 0, the count is incremented. Finally, the function returns the count.

The `main` function is used to test the `CountNums` function with different input arrays. The results are printed to the console.