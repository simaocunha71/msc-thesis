Here is the solution in Go:
```go
package main

import (
    "strconv"
)

func Specialfilter(nums []int) int {
    count := 0
    for _, num := range nums {
        str := strconv.Itoa(num)
        if num > 10 {
            if str[0]%2 != 0 && str[len(str)-1]%2 != 0 {
                count++
            }
        }
    }
    return count
}

func main() {
    nums := []int{15, -73, 14, -15}
    result := Specialfilter(nums)
    println(result) // Output: 1

    nums = []int{33, -2, -3, 45, 21, 109}
    result = Specialfilter(nums)
    println(result) // Output: 2
}
```
The function `Specialfilter` iterates over the input array `nums` and checks each number. If the number is greater than 10, it converts the number to a string `str` and checks if the first and last digits are odd (i.e., `str[0]%2 != 0 && str[len(str)-1]%2 != 0`). If both conditions are true, it increments the count. Finally, it returns the count.

In the `main` function, we test the `Specialfilter` function with two examples and print the results. The output should be `1` for the first example and `2` for the second example.