Here is a possible implementation of the `SortNumbers` function in Go:

```go
package main

import (
    "fmt"
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
    numSlice := strings.Split(numbers, " ")

    // Define a mapping of number strings to their integer values
    numMap := map[string]int{
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    // Use the map to convert the slice of strings to a slice of integers
    intSlice := make([]int, len(numSlice))
    for i, num := range numSlice {
        intSlice[i] = numMap[num]
    }

    // Sort the slice of integers
    sort.Ints(intSlice)

    // Use the map to convert the slice of integers back to a slice of strings
    sortedNumSlice := make([]string, len(intSlice))
    for i, num := range intSlice {
        for k, v := range numMap {
            if v == num {
                sortedNumSlice[i] = k
                break
            }
        }
    }

    // Join the sorted slice of strings back into a single string
    sortedNumbers := strings.Join(sortedNumSlice, " ")

    return sortedNumbers
}

func main() {
    fmt.Println(SortNumbers("three one five"))
}
```

This code splits the input string into a slice of strings, converts each string to an integer using a map, sorts the slice of integers, and then converts the sorted integers back to strings using the same map. The sorted slice of strings is then joined back into a single string and returned as the result. The `main` function demonstrates the use of the `SortNumbers` function. When run, this