Here is a Go solution that uses a loop to iterate over the input array and checks each number to see if it is greater than 10 and if both the first and last digits of the number are odd.

```go
package main

import (
    "fmt"
    "strconv"
)

// Write a function that takes an array of numbers as input and returns
// the number of elements in the array that are greater than 10 and both
// first and last digits of a number are odd (1, 3, 5, 7, 9).
// For example:
// Specialfilter([15, -73, 14, -15]) => 1
// Specialfilter([33, -2, -3, 45, 21, 109]) => 2
func Specialfilter(nums []int) int {

    var count int
    for _, num := range nums {
        if num > 10 {
            numStr := strconv.Itoa(num)
            if (numStr[0] - '0')%2 != 0 && (numStr[len(numStr)-1] - '0')%2 != 0 {
                count++
            }
        }
    }
    return count
}

func main() {
    fmt.Println(Specialfilter([]int{15, -73, 14, -15})) // Output: 1
    fmt.Println(Specialfilter([]int{33, -2, -3, 45, 21, 109})) // Output: 2
}
```

The function `Specialfilter` takes a slice of integers as input and returns the count of numbers that meet the conditions. It iterates over each number in the input array, checks if the number is greater than 10, and if so, converts the number to a string to easily access the first and last digits. It then checks if the first and last digits are odd by subtracting the ASCII value of '0' from the character and taking the modulus with 2. If both conditions are met, it increments the count. Finally, it returns the count. The `main` function demonstrates the usage of the `Specialfilter` function.