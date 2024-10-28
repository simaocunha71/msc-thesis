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
    // Split the input string into a slice of strings
    words := strings.Split(numbers, " ")
    
    // Define a function to compare two strings
    type compareFunc func(string, string) bool
    sortFunc := func(i, j int) bool {
        var num1 int
        var num2 int
        switch words[i] {
        case "zero":
            num1 = 0
        case "one":
            num1 = 1
        case "two":
            num1 = 2
        case "three":
            num1 = 3
        case "four":
            num1 = 4
        case "five":
            num1 = 5
        case "six":
            num1 = 6
        case "seven":
            num1 = 7
        case "eight":
            num1 = 8
        case "nine":
            num1 = 9
        }
        switch words[j] {
        case "zero":
            num2 = 0
        case "one":
            num2 = 1
        case "two":
            num2 = 2
        case "three":
            num2 = 3
        case "four":
            num2 = 4
        case "five":
            num2 = 5
        case "six":
            num2 = 6
        case "seven":
            num2 = 7
        case "eight":
            num2 = 8
        case "nine":
            num2 = 9
        }
        return num1 < num2
    }
    
    // Sort the slice of strings
    sort.Slice(words, sortFunc)
    
    // Join the sorted slice of strings into a single string
    sortedNumbers := strings.Join(words, " ")
    
    return sortedNumbers
}
```


The solution works by first splitting the input string into a slice of strings using the `strings.Split` function