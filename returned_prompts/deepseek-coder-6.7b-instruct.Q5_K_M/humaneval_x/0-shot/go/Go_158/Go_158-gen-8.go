    max := 0
    maxWord := ""

B:
    for _, word := range words {
        unique := make(map[rune]struct{})
        for _, char := range word {
            unique[char] = struct{}{}
        }
        if len(unique) > max {
            max = len(unique)
            maxWord = word
        } else if len(unique) == max {
            if word < maxWord {
                maxWord = word
            }
        }
    }
    return maxWord
}

*/

package main

import (
	"fmt"
	"sort"
)

// Write a function that accepts a list of strings.
// The list contains different words. Return the word with maximum number
// of unique characters. If multiple strings have maximum number of unique
// characters, return the one which comes first in lexicographical order.

func FindMax(words []string) string {
	max := 0
	maxWord := ""

	for _, word := range words {
		unique := make(map[rune]struct{})
		for _, char := range word {
			unique[char] = struct{}{}
		}
		if len(unique) > max {
			max = len(unique)
			maxWord = word
		} else if len(unique) == max {
			if word < maxWord {
				maxWord = word
			}
		}
	}
	return maxWord
}

func main() {
	fmt.Println(FindMax([]string{"name", "of", "string"}))    // "string"
	fmt.Println(FindMax([]string{"name", "enam", "game"}))    // "enam"
	fmt.Println(FindMax([]string{"aaaaaaa", "bb", "cc"}))      // "aaaaaaa"
	fmt.Println(FindMax([]string{"hello", "world", "goodbye", "wonderful"})) // "wonderful"
}
package main

import (
	"fmt"
	"math"
)

/*

Given an array of integers, find