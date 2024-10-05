Here is the Go function that meets the requirements:
```go
package main

import (
    "strconv"
)

func Specialfilter(nums []int) int {
    count := 0
    for _, num := range nums {
        str := strconv.Itoa(num)
        if num > 10 && (str[0] % 2 != 0 && str[len(str)-1] % 2 != 0) {
            count++
        }
    }
    return count
}

func main() {
    nums := []int{15, -73, 14, -15}
    result := Specialfilter(nums)
    println(result)  // Output: 1

    nums = []int{33, -2, -3, 45, 21, 109}
    result = Specialfilter(nums)
    println(result)  // Output: 2
}
```
Explanation:

1. Initialize a counter variable `count` to 0.
2. Iterate through each element `num` in the input array `nums`.
3. Convert the integer `num` to a string `str` using the `strconv.Itoa` function.
4. Check if the number is greater than 10 and both the first and last digits of the number are odd (1, 3, 5, 7, 9). This is done by checking if the remainder of the division of the first and last characters of the string by 2 is not equal to 0.
5. If the condition is true, increment the `count` variable.
6. Return the final value of `count`.

In the example code, we test the function with two input arrays and print the results. The function returns the correct count of elements that meet the condition in both cases.