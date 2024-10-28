    splitString := strings.Fields(s)
    
    for i, word := range splitString {
        sortWord := []rune(word)
        sort.Slice(sortWord, func(i, j int) bool {
            return sortWord[i] < sortWord[j]
        })
        splitString[i] = string(sortWord)
    }

    return strings.Join(splitString, " ")
}

*/

package main

import (
	"fmt"
	"strings"
	"sort"
)

func AntiShuffle(s string) string  {
    splitString := strings.Fields(s)
    
    for i, word := range splitString {
        sortWord := []rune(word)
        sort.Slice(sortWord, func(i, j int) bool {
            return sortWord[i] < sortWord[j]
        })
        splitString[i] = string(sortWord)
    }

    return strings.Join(splitString, " ")
}

func main() {
	fmt.Println(AntiShuffle("Hello World!!!"))
}

/*
func AntiShuffle(s string) string {
	splitString := strings.Fields(s)

	for i, word := range splitString {
		runes := []rune(word)
		sort.Slice(runes, func(i, j int) bool {
			return runes[i] < runes[j]
		})
		splitString[i] = string(runes)
	}

	return strings.Join(splitString, " ")
}
*/

/*
func AntiShuffle(s string) string  {
    splitString := strings.Fields(s)
    
    for i, word := range splitString {
        sortWord := []rune(word)
        sort.Slice(sortWord, func(i, j int) bool {
            return sortWord[i] < sortWord[j]
        })
        splitString[i] = string(sortWord)
    }

    return strings.Join(splitString, " ")