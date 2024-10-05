    lowerStr := strings.ToLower(str)
    count := make(map[rune]int)
    for _, char := range lowerStr {
        count[char]++
    }
    return len(count)
}

*/

import (
	"strings"
)

func CountDistinctCharacters(str string) int {
	lowerStr := strings.ToLower(str)
	count := make(map[rune]int)
	for _, char := range lowerStr {
		count[char]++
	}
	return len(count)
}

func main() {
	fmt.Println(CountDistinctCharacters("xyzXYZ"))
	fmt.Println(CountDistinctCharacters("Jerry"))
}

*/

/*
// 1.8.6: Write a function that takes as input a string and returns a boolean value indicating whether the string is a palindrome.

// A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.

//  For example:

//  IsPalindrome("racecar") // returns true
//  IsPalindrome("hello") // returns false

