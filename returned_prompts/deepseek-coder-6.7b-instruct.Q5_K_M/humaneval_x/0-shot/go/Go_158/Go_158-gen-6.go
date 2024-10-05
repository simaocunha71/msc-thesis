     maxWord := ""
     maxCount := 0

B:
     for _, word := range words {
         count := getUniqueChars(word)
         if count > maxCount {
             maxCount = count
             maxWord = word
         } else if count == maxCount && word < maxWord {
             maxWord = word
         }
     }

C:
     return maxWord
}

func getUniqueChars(word string) int {
     m := make(map[rune]bool)

E:
     for _, char := range word {
         m[char] = true
     }

F:
     return len(m)
}

Explanation:
The function FindMax iterates over the list of words and for each word it
determines the number of unique characters using getUniqueChars function.
If the number of unique characters of the current word is greater than the
maxCount, the word is saved as maxWord and maxCount is updated with the
number of unique characters of the current word. If the number of unique
characters of the current word is equal to maxCount, the function checks
whether the current word comes before maxWord lexicographically and if it
does, maxWord is updated with the current word. Finally, maxWord is returned.

The function getUniqueChars creates a map to store the unique characters of
the word and returns the length of the map as the number of unique characters.

The time complexity of this function is O(n*m), where n is the number of words
and m is the average length of the words. The space complexity is O(n*m) as
well, because of the map used in getUniqueChars function.
*/
package main

import (
	"fmt"
)

func FindMax(words []string) string {
	maxWord := ""
	maxCount := 0

	for _, word := range words {
		count := getUniqueChars(word)
		if count > maxCount {
			maxCount = count
			maxWord = word
		} else if count == maxCount && word < maxWord {
			maxWord = word
		}
	}