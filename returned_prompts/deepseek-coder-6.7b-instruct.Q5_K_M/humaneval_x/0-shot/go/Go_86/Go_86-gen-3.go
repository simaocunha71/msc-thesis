    words := strings.Fields(s)
    for i, word := range words {
        chars := strings.Split(word, "")
        sort.Strings(chars)
        words[i] = strings.Join(chars, "")
    }
    return strings.Join(words, " ")
}

func main() {
    fmt.Println(AntiShuffle("Hello World!!!"))
}

The function AntiShuffle receives a string, splits it into words, sorts each word's characters, and then joins them back together. 
The function sort.Strings sorts the characters of the word in ascending order based on their ascii value. 
The function strings.Fields splits the string into words by spaces and returns a slice of words. 
The function strings.Join concatenates the words in the slice with a space in between.
*/

import (
	"fmt"
	"sort"
	"strings"
)

func AntiShuffle(s string) string {
	words := strings.Fields(s)
	for i, word := range words {
		chars := strings.Split(word, "")
		sort.Strings(chars)
		words[i] = strings.Join(chars, "")
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
The function AntiShuffle takes a string and splits it into words. It then sorts each word's characters in ascending order based on their ascii value, and joins them back together with a space in between.
The function strings.Fields splits the string into words by spaces and returns a slice of words.
The function strings.Split splits a string into a slice of substrings, where each substring is a single character from the original string.
The function sort.Strings sorts a slice of strings in ascending order.
The function strings.Join concatenates the words in the slice with a space in between.
*/

/*
