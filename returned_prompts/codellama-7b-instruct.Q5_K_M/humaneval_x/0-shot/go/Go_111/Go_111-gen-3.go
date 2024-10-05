import (
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
    var runes []rune
    var letter rune
    var count int
    var result map[rune]int
    var maxCount int

    // Convert string to a slice of runes
    runes = []rune(test)

    // Initialize result map
    result = make(map[rune]int)

    // Iterate through the runes
    for i, rune := range runes {
        letter = rune
        count++
        // If the letter already exists in the map
        if _, ok := result[letter]; ok {
            // Increment the count
            result[letter]++
        } else {
            // Otherwise, set the count
            result[letter] = 1
        }
        // If the count is greater than the maximum count
        if count > maxCount {
            // Set the maximum count
            maxCount = count
        }
        // If the letter is a space
        if letter == ' ' {
            // Reset the count
            count = 0
        }
    }
    return result
}
