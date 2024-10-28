    var result []string
    words := strings.Split(s, " ")
    for _, word := range words {
        count := 0
        for _, letter := range word {
            if strings.ContainsRune("aeiouAEIOU", letter) {
                continue
            }
            count++
        }
        if count == n {
            result = append(result, word)
        }
    }
    return result
}

func main() {
    fmt.Println(SelectWords("Mary had a little lamb", 4)) // ["little"]
    fmt.Println(SelectWords("Mary had a little lamb", 3)) // ["Mary", "lamb"]
    fmt.Println(SelectWords("simple white space", 2)) // []
    fmt.Println(SelectWords("Hello world", 4)) // ["world"]
    fmt.Println(SelectWords("Uncle sam", 3)) // ["Uncle"]
}

*/

package main

import (
	"fmt"
	"strings"
)

// Given a string s and a natural number n, you have been tasked to implement
// a function that returns a list of all words from string s that contain exactly
// n consonants, in order these words appear in the string s.
// If the string s is empty then the function should return an empty list.
// Note: you may assume the input string contains only letters and spaces.
// Examples:
// SelectWords("Mary had a little lamb", 4) ==> ["little"]
// SelectWords("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
// SelectWords("simple white space", 2) ==> []
// SelectWords("Hello world", 4) ==> ["world"]
// SelectWords("Uncle sam", 3) ==> ["Uncle"]
func SelectWords(s string, n int) []string {
	var result []string
	words := strings.Split(s, " ")
	for _, word := range words {
		count := 0
		for _, letter := range word {
			if strings.