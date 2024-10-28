Here is the solution:

```go
import (
    "sort"
    "strings"
)

// Input is a space-delimited string of numberals from 'zero' to 'nine'.
// Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
// Return the string with numbers sorted from smallest to largest
// >>> SortNumbers('three one five')
// 'one three five'
func SortNumbers(numbers string) string {
    // Split the input string into a slice of strings, each representing a number
    numSlice := strings.Split(numbers, " ")

    // Create a slice of integers, where each integer represents a number
    intSlice := make([]int, 0, len(numSlice))
    for _, num := range numSlice {
        switch num {
        case "zero":
            intSlice = append(intSlice, 0)
        case "one":
            intSlice = append(intSlice, 1)
        case "two":
            intSlice = append(intSlice, 2)
        case "three":
            intSlice = append(intSlice, 3)
        case "four":
            intSlice = append(intSlice, 4)
        case "five":
            intSlice = append(intSlice, 5)
        case "six":
            intSlice = append(intSlice, 6)
        case "seven":
            intSlice = append(intSlice, 7)
        case "eight":
            intSlice = append(intSlice, 8)
        case "nine":
            intSlice = append(intSlice, 9)
        }
    }

    // Sort the slice of integers
    sort.Ints(intSlice)

    // Convert the slice of integers back to a slice of strings
    sortedNumSlice := make([]string, 0, len(intSlice))
    for _, num := range intSlice {
        switch num {
        case 0:
            sortedNumSlice = append(sortedNumSlice, "zero")
        case 1:
            sortedNumSlice = append(sortedNumSlice, "one")
        case 2:
            sortedNumSlice = append(sortedNumSlice, "two")
        case 3:
            sortedNumSlice = append(sortedNumSlice, "three")
        case 4:
            sortedNumSlice = append(sortedNumSlice, "four")
        case 5:
            sortedNumSlice = append(sortedNumSlice, "five")
        case 6