Here is the solution in Go:

```go
package main

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
    // Split the input string into a slice of strings
    words := strings.Split(numbers, " ")

    // Create a slice of integers from the words
    nums := make([]int, len(words))
    for i, word := range words {
        switch word {
        case "zero":
            nums[i] = 0
        case "one":
            nums[i] = 1
        case "two":
            nums[i] = 2
        case "three":
            nums[i] = 3
        case "four":
            nums[i] = 4
        case "five":
            nums[i] = 5
        case "six":
            nums[i] = 6
        case "seven":
            nums[i] = 7
        case "eight":
            nums[i] = 8
        case "nine":
            nums[i] = 9
        }
    }

    // Sort the slice of integers
    sort.Ints(nums)

    // Create a new slice of strings with the sorted numbers
    sortedWords := make([]string, len(nums))
    for i, num := range nums {
        switch num {
        case 0:
            sortedWords[i] = "zero"
        case 1:
            sortedWords[i] = "one"
        case 2:
            sortedWords[i] = "two"
        case 3:
            sortedWords[i] = "three"
        case 4:
            sortedWords[i] = "four"
        case 5:
            sortedWords[i] = "five"
        case 6:
            sortedWords[i] = "six"
        case 7:
            sortedWords[i] = "seven"
        case 8:
            sortedWords[i] = "eight"
        case 9:
            sortedWords[i] = "nine"
        }
    }

    // Join the sorted words back into a string
    result := strings