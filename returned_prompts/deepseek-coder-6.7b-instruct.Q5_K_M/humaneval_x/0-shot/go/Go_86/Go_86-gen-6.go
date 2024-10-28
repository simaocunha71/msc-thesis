     words := strings.Fields(s)
B:
     for i, word := range words {
         chars := []rune(word)
         sort.Slice(chars, func(i, j int) bool {
             return chars[i] < chars[j]
         })
         words[i] = string(chars)
     }
C:
     return strings.Join(words, " ")
}

// Testing the function
func main() {
    fmt.Println(AntiShuffle("Hello World!!!"))
}

*/

import (
	"fmt"
	"sort"
	"strings"
)

func AntiShuffle(s string) string {
	words := strings.Fields(s)

	for i, word := range words {
		chars := []rune(word)
		sort.Slice(chars, func(i, j int) bool {
			return chars[i] < chars[j]
		})
		words[i] = string(chars)
	}

	return strings.Join(words, " ")
}

func main() {
	fmt.Println(AntiShuffle("Hello World!!!"))
}

/*
Output:
Hello  !!!Wdlor
*/

/*
Explanation:
The function `AntiShuffle(s string) string` takes a string as an argument and returns a string with all the words sorted in ascending order based on their ASCII values.
The function `AntiShuffle` first splits the input string into words using `strings.Fields(s)`.
Then it sorts each word character by character using `sort.Slice(chars, func(i, j int) bool { return chars[i] < chars[j] })`.
Finally, it joins all the sorted words back into a single string using `strings.Join(words, " ")`.
This function is case sensitive and does not handle punctuation.
*/

/*
This function works by first splitting the input string into words. Then, for each word, it converts it to a slice of runes (characters). The sort.Slice function is