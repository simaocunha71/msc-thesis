To solve this problem, you can follow these steps:

1. Split the input string into individual words using the `strings.Fields` function.
2. Create a map to map each word to its corresponding number.
3. Create an empty slice to store the numbers.
4. Iterate through the words and convert each word to its corresponding number using the map.
5. Sort the slice of numbers.
6. Create an empty string to store the result.
7. Iterate through the sorted slice and append each number to the result string.
8. Return the result string.

Here's the complete implementation of the `SortNumbers` function:

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
    // Create a map to map each word to its corresponding number
    wordToNumber := map[string]int{
        "zero":   0,
        "one":    1,
        "two":    2,
        "three":  3,
        "four":   4,
        "five":   5,
        "six":    6,
        "seven":  7,
        "eight":  8,
        "nine":   9,
    }

    // Split the input string into individual words
    words := strings.Fields(numbers)

    // Create an empty slice to store the numbers
    numbersSlice := make([]int, len(words))

    // Convert each word to its corresponding number
    for i, word := range words {
        numbersSlice[i] = wordToNumber[word]
    }

    // Sort the slice of numbers
    sort.Ints(numbersSlice)

    // Create an empty string to store the result
    result := ""

    // Append each number to the result string
    for _, number := range numbersSlice {
        result += string(number) + " "
    }

    // Remove the trailing space
    result = strings.TrimSuffix(result, " ")

    // Return the result string
    return result
}
```

Now you can test the `SortNumbers` function with different inputs:

```go