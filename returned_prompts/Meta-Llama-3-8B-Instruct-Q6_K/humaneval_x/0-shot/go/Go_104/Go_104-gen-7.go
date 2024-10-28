Here is a Go function that solves the problem:

```go
import (
    "sort"
    "strconv"
)

func UniqueDigits(x []int) []int {
    var result []int
    for _, num := range x {
        str := strconv.Itoa(num)
        hasEvenDigit := false
        for _, c := range str {
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

This function iterates over each number in the input slice. For each number, it converts it to a string and checks each character (digit) to see if it's even. If it finds a digit that is even, it sets a flag to true and breaks out of the inner loop. If the flag is still false after checking all digits, it adds the number to the result slice. Finally, it sorts the result slice in ascending order and returns it.

The time complexity of this function is O(n*m), where n is the length of the input slice and m is the maximum number of digits in a number. The space complexity is O(n), where n is the number of numbers in the input slice that don't have any even digits. 

Note that the function uses the `strconv` package to convert between strings and integers, and the `sort` package to sort the result slice. It also uses the `range` keyword to iterate over the characters in a string, and the `break` statement to exit the inner loop early. 

You can test this function with the examples you provided to see that it produces the correct results. For example:

```go
x := []int{15, 33, 1422, 1}
result := UniqueDigits(x)
fmt.Println(result) // Output: [1 15 33]

x = []int{152, 323, 1422, 10}
result = UniqueDigits(x)
fmt.Println(result) // Output: []
``` 