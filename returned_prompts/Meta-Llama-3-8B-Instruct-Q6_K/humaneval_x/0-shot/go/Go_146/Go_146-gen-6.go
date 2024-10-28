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
            str := strconv.Itoa(num)
            if len(str) > 1 && (str[0] % 2 != 0 && str[len(str)-1] % 2 != 0) {
                count++
            }
        }
    }
    return count
}

func main() {
    fmt.Println(Specialfilter([]int{15, -73, 14, -15}))  // Output: 1
    fmt.Println(Specialfilter([]int{33, -2, -3, 45, 21, 109}))  // Output: 2
}
```



The function Specialfilter takes a slice of integers as an argument and returns the number of elements in the slice that are greater than 10 and both the first and last digits of the number are odd.

The function iterates over each number in the slice. For each number, it converts the number to a string and checks if the number is greater than 10. If it is, it checks if the first and last digits of the number are odd by checking if the remainder of the division of the digit by 2 is not 0. If both conditions are true, it increments the count.

Finally, the function returns the count.

In the main function, we test the Specialfilter function with two slices of integers and print the results. The output is 1 for the first slice and 2 for the second slice.