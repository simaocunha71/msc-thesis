    for _, word := range strings.Fields(sentence) {
        if len(word) < 2 {
            continue A
        }
        for i := 2; i*i <= len(word); i++ {
            if len(word)%i == 0 {
                continue A
            }
        }
        return word
    }
    return ""
}

*/

/*

import (
	"fmt"
	"strings"
)

// You are given a string representing a sentence,
// the sentence contains some words separated by a space,
// and you have to return a string that contains the words from the original sentence,
// whose lengths are prime numbers,
// the order of the words in the new string should be the same as the original one.
// 
// Example 1:
// Input: sentence 
= "This is a test"
// Output: "is"
// 
// Example 2:
// Input: sentence = "lets go for swimming"
// Output: "go for"
// 
// Constraints:
// 1 ≤