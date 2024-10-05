Here is a possible implementation of the `SortNumbers` function in Go:
```go
package main

import (
    "sort"
    "strings"
)

func SortNumbers(numbers string) string {
    // Split the input string into individual numbers
    nums := strings.Split(numbers, " ")

    // Convert each number to an integer and store them in a slice
    numSlice := make([]int, 0, len(nums))
    for _, num := range nums {
        switch num {
        case "zero":
            numSlice = append(numSlice, 0)
        case "one":
            numSlice = append(numSlice, 1)
        case "two":
            numSlice = append(numSlice, 2)
        case "three":
            numSlice = append(numSlice, 3)
        case "four":
            numSlice = append(numSlice, 4)
        case "five":
            numSlice = append(numSlice, 5)
        case "six":
            numSlice = append(numSlice, 6)
        case "seven":
            numSlice = append(numSlice, 7)
        case "eight":
            numSlice = append(numSlice, 8)
        case "nine":
            numSlice = append(numSlice, 9)
        }
    }

    // Sort the slice of numbers
    sort.Ints(numSlice)

    // Convert the sorted slice of numbers back to a string
    result := make([]string, 0, len(numSlice))
    for _, num := range numSlice {
        switch num {
        case 0:
            result = append(result, "zero")
        case 1:
            result = append(result, "one")
        case 2:
            result = append(result, "two")
        case 3:
            result = append(result, "three")
        case 4:
            result = append(result, "four")
        case 5:
            result = append(result, "five")
        case 6:
            result = append(result, "six")
        case 7:
            result = append(result, "seven")
        case 8:
            result = append(result, "eight")
        case 9:
            result = append(result, "nine")
        }
    }

    // Join the sorted slice of numbers into a single string
    return strings.Join(result, " ")
}

func main() {
    input := "three one five"
    output := SortNumbers(input)
    println(output) // Output: one