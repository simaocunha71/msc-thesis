    split := strings.Split(s, " ")
    for i := range split {
        chars := strings.Split(split[i], "")
        sort.Strings(chars)
        split[i] = strings.Join(chars, "")
    }
    return strings.Join(split, " ")
}

func main() {
    fmt.Println(AntiShuffle("Hello World!!!")) // Expected output: "Hello  !!!Wdlor"
}
*/

import (
	"fmt"
	"sort"
	"strings"
)

// Write a function that takes a string and returns an ordered version of it.
// Ordered version of string, is a string where all words (separated by space)
// are replaced by a new word where all the characters arranged in
// ascending order based on ascii value.
// Note: You should keep the order of words and blank spaces in the sentence.
// 
// For example:
// AntiShuffle('Hi') returns  'Hi'
// AntiShuffle('hello') returns 'ehllo'
// AntiShuffle('Hello World!!!') returns 'Hello  !!!Wdlor'
func AntiShuffle(s string) string {
	split := strings.Split(s, " ")
	for i := range split {
		chars := strings.Split(split[i], "")
		sort.Strings(chars)
		split[i] = strings.Join(chars, "")
	}
	return strings.Join(split, " ")
}

func main() {
	fmt.Println(AntiShuffle("Hello World!!!")) // Expected output: "Hello  !!!Wdlor"
}

// This code first splits the input string into words. For each word, it splits the word into characters, sorts the characters in ascending order, then joins them back together into a sorted word. Finally, it joins the sorted words back together into a string, maintaining the original word order and blank spaces.
// 
// The time complexity of this code is O(n log n), where n is the length of the input string. This is because the code contains a sort operation that takes O