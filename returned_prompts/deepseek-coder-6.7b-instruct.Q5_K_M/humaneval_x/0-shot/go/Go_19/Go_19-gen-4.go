    // Create a map to convert words to numbers
    wordNum := map[string]int{
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

B:
    // Split the input string into a slice of words
    words := strings.Split(numbers, " ")

C:
    // Map each word in the slice to its corresponding number
    wordNums := make([]int, len(words))
    for i, word := range words {
        wordNums[i] = wordNum[word]
    }

D:
    // Sort the numbers
    sort.Ints(wordNums)

E:
    // Convert the sorted numbers back to words
    for i, num := range wordNums {
        words[i] = getKey(wordNum, num)
    }

F:
    // Join the words back into a string and return
    return strings.Join(words, " ")
}

// getKey is a helper function that returns the key of a map given a value.
func getKey(m map[string]int, value int) string {
    for k, v := range m {
        if v == value {
            return k
        }
    }
    return ""
}

This program takes in a string of words representing numbers from 0 to 9, and returns the string sorted in ascending order.

The helper function getKey is used to convert a number back to its corresponding word.
*/
package main

import (
	"fmt"
)

func main() {
	fmt.Println(SortNumbers("three one five"))
	// Output: "one three five"
}

func SortNumbers(numbers string) string {
	wordNum := map[string]int{
		"zero":  0,
		"one":   1,
		"two":   2,
	