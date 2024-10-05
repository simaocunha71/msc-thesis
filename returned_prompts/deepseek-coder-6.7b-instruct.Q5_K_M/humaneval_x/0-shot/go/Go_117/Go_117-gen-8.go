    if len(s) == 0 {
        return []string{}
    }

B:
    words := strings.Fields(s)

C:
    var result []string
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

D:
    return result
}


A: Check if the string s is empty. If so, return an empty slice.
B: Split the string s into a slice of words.
C: Iterate over each word in the slice of words. For each word, count the number of consonants by iterating over each letter in the word. If the letter is not a vowel, increment the count. If the count of consonants in the word equals n, append the word to the result slice.
D: Return the result slice.
*/

package main

import (
	"fmt"
)

func SelectWords(s string, n int) []string {
	if len(s) == 0 {
		return []string{}
	}

	words := strings.Fields(s)
	var result []string
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
	fmt.Println(SelectWords("simple white space", 2))    // []
	fmt.Println(SelectWords("Hello world", 4))            // ["world"]
	fmt.Println(SelectWords