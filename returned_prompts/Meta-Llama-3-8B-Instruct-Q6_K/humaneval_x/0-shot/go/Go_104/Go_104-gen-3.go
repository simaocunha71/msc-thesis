Here is a Go solution for the problem:

```go
import (
    "sort"
    "strconv"
)

func UniqueDigits(x []int) []int {
    var result []int
    for _, num := range x {
        s := strconv.Itoa(num)
        hasEvenDigit := false
        for _, c := range s {
            digit, _ := strconv.Atoi(string(c))
            if digit%2 == 0 {
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

This function iterates over each number in the input slice. For each number, it converts it to a string and checks each character (digit) in the string to see if it's even. If any digit is even, it sets a flag to true. If no even digits are found, it appends the number to the result slice. After all numbers have been checked, it sorts the result slice and returns it. 

The time complexity of this function is O(n*m), where n is the length of the input slice and m is the maximum length of a number in the slice. This is because for each number, we're iterating over each digit in the number. The space complexity is O(n), as we're storing the result in a slice. 

Note that this function returns a slice of integers, as required by the problem. It also sorts the result slice in ascending order, as required by the problem. 

You can test this function with the examples you provided:

```go
fmt.Println(UniqueDigits([]int{15, 33, 1422, 1})) // [1, 15, 33]
fmt.Println(UniqueDigits([]int{152, 323, 1422, 10})) // []
```  