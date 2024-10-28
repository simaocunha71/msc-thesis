import (
    "fmt"
    "strings"
)

// Given a string representing a space separated lowercase letters, return a dictionary
// of the letter with the most repetition and containing the corresponding count.
// If several letters have the same occurrence, return all of them.
// 
// Example:
// Histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
// Histogram('a b b a') == {'a': 2, 'b': 2}
// Histogram('a b c a b') == {'a': 2, 'b': 2}
// Histogram('b b b b a') == {'b': 4}
// Histogram('') == {}
func Histogram(test string) map[rune]int {

    // your code here
    // map[rune]int
    letter_count := make(map[rune]int)
    string_array := strings.Split(test, " ")
    for _, string_element := range string_array {
        letter_count[rune(string_element[0])]++
    }

    max_count := 0
    max_count_letter := ""
    for letter, count := range letter_count {
        if count > max_count {
            max_count = count
            max_count_letter = letter
        }
    }

    fmt.Println("Letter:", max_count_letter, "Count:", max_count)

    return letter_count
}

