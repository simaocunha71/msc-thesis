Here is a possible solution in Go:
```go
package main

import (
    "fmt"
    "sort"
    "strings"
)

func SortNumbers(numbers string) string {
    // Split the input string into a slice of strings
    parts := strings.Split(numbers, " ")

    // Convert each string to an integer and sort the slice
    numbers := make([]int, len(parts))
    for i, part := range parts {
        switch part {
        case "zero":
            numbers[i] = 0
        case "one":
            numbers[i] = 1
        case "two":
            numbers[i] = 2
        case "three":
            numbers[i] = 3
        case "four":
            numbers[i] = 4
        case "five":
            numbers[i] = 5
        case "six":
            numbers[i] = 6
        case "seven":
            numbers[i] = 7
        case "eight":
            numbers[i] = 8
        case "nine":
            numbers[i] = 9
        }
    }
    sort.Ints(numbers)

    // Convert the sorted slice back to a string
    result := ""
    for _, num := range numbers {
        switch num {
        case 0:
            result += "zero "
        case 1:
            result += "one "
        case 2:
            result += "two "
        case 3:
            result += "three "
        case 4:
            result += "four "
        case 5:
            result += "five "
        case 6:
            result += "six "
        case 7:
            result += "seven "
        case 8:
            result += "eight "
        case 9:
            result += "nine "
        }
    }
    result = strings.TrimSpace(result)

    return result
}

func main() {
    fmt.Println(SortNumbers("three one five")) // Output: "five one three"
}
```
This solution first splits the input string into a slice of strings using the `strings.Split` function. Then, it converts each string to an integer using a switch statement. The slice of integers is then sorted using the `sort.Ints` function. Finally, the sorted slice is converted back to a string using another switch statement, and the resulting string is returned. In the `main` function, we test the `SortNumbers` function with the input string "three one five". The output