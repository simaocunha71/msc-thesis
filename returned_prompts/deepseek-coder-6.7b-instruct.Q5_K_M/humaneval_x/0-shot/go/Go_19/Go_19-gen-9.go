    words := strings.Split(numbers, " ")

B:
    sort.Slice(words, func(i, j int) bool {
        return numToWord[words[i]] < numToWord[words[j]]
    })

C:
    return strings.Join(words, " ")

}

var numToWord = map[string]int{
    "zero":  0,
    "one":   1,
    "two":   2,
    "three": 3,
    "four":  4,
    "five":  5,
    "six":   6,
    "seven": 7,
    "eight": 8,
    "nine":  9,
}

func main() {
    fmt.Println(SortNumbers("three one five"))
}

This code first splits the input string into a slice of words. Then it sorts the slice based on the value mapped in the numToWord map. Finally, it joins the sorted words back into a single string, separated by spaces.
*/

package main

import (
	"fmt"
	"sort"
	"strings"
)

var numToWord = map[string]int{
	"zero":  0,
	"one":   1,
	"two":   2,
	"three": 3,
	"four":  4,
	"five":  5,
	"six":   6,
	"seven": 7,
	"eight": 8,
	"nine":  9,
}

// SortNumbers sorts a string of numbers from 'zero' to 'nine' in ascending order.
func SortNumbers(numbers string) string {
	words := strings.Split(numbers, " ")

	sort.Slice(words, func(i, j int) bool {
		return numToWord[words[i]] < numToWord[words[j]]
	})

	return strings.Join(words, " ")
}

func main() {
	fmt.Println(SortNumbers("three one five"))
}

// Output: "one three five"

/* Explanation:
The SortNumbers function takes a