Here is a Go solution using a slice to store the numbers that don't have any even digits. We iterate over the input slice, check each number for even digits, and if it doesn't have any, we add it to our result slice. Finally, we sort the result slice and return it.

```go
import (
    "sort"
    "strconv"
)

// Given a list of positive integers x. return a sorted list of all
// elements that hasn't any even digit.
// 
// Note: Returned list should be sorted in increasing order.
// 
// For example:
// >>> UniqueDigits([15, 33, 1422, 1])
// [1, 15, 33]
// >>> UniqueDigits([152, 323, 1422, 10])
// []
func UniqueDigits(x []int) []int {

    var result []int
    for _, num := range x {
        str := strconv.Itoa(num)
        hasEvenDigit := false
        for _, c := range str {
            if digit, err := strconv.Atoi(string(c)); err == nil && digit%2 == 0 {
                hasEvenDigit = true
                break
            }
        }
        if !hasEvenDigit {
            result = append(result, num)
        }
    }

    sort.Ints(result)
    return result
}
```


This function works by iterating over each number in the input slice, converting it to a string, and then iterating over each character (digit) in the string. If any of these digits are even (i.e., the remainder when divided by 2 is 0), we set a flag to true. If no even digits are found, we add the number to our result slice. Finally, we sort the result slice and return it. The time complexity is O(n*m), where n is the number of elements in the input slice and m is the maximum number of digits in a number. The space complexity is O(n), where n is the number of elements in the result slice.