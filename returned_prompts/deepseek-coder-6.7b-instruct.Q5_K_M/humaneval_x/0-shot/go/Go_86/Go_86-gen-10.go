    splitWords := strings.Fields(s)

B:
    for i, word := range splitWords {
        splitWords[i] = shuffleWord(word)
    }

C:
    return strings.Join(splitWords, " ")
}

func shuffleWord(word string) string {

D:
    chars := []rune(word)

E:
    sort.Slice(chars, func(i, j int) bool {
        return chars[i] < chars[j]
    })

F:
    return string(chars)
}

The program takes a string as input, splits it into words using strings.Fields function, 
then uses a for loop to iterate over the words and applies the shuffleWord function 
which sorts the characters in each word in ascending order, then joins the words back 
together with a space separator and returns the result.
*/

package main

import (
	"fmt"
)

func AntiShuffle(s string) string {
	splitWords := strings.Fields(s)

	for i, word := range splitWords {
		splitWords[i] = shuffleWord(word)
	}

	return strings.Join(splitWords, " ")
}

func shuffleWord(word string) string {
	chars := []rune(word)

	sort.Slice(chars, func(i, j int) bool {
		return chars[i] < chars[j]
	})

	return string(chars)
}

func main() {
	fmt.Println(AntiShuffle("Hello World!!!"))
}

// Output: "Hello  !!!Wdlor"




























































































