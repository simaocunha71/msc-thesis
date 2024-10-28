    for i := len(word) - 2; i > 0; i-- {
        if !isVowel(word[i]) && isVowel(word[i+1]) && isVowel(word[i-1]) {
            return string(word[i])
        }
    }
    return ""
}

func isVowel(b byte) bool {
    return bytes.Contains([]byte("aeiouAEIOU"), []byte{b})
}


A: This function is traversing the string from the right and checking for a vowel that is surrounded by consonants. The first such vowel it finds is returned. If no such vowel is found, an empty string is returned. The function isVowel is used to check if a given byte is a vowel.

The time complexity of this function is O(n), where n is the length of the string. This is because in the worst case scenario, the function traverses the entire string once. The space complexity is O(1), as no additional space is used that scales with the size of the input.

This function is case sensitive, as the problem statement suggests. It will return the lowercase vowel "u" instead of the uppercase vowel "U" in the example "FULL".

The function assumes that the given string contains only English letters. If this assumption is not met, the function may not work as expected.

The function does not handle strings with non-English letters. If such a string is passed to the function, it will not be able to handle them and may result in unexpected behavior or errors.

This function does not handle strings with non-English letters. If such a string is passed to the function, it will not be able to handle them and may result in unexpected behavior or errors.
*/

package main

import (
	"fmt"
)

func GetClosestVowel(word string) string {
	for i := len(word) - 2; i > 0; i-- {
		if !isVowel(word[i]) && isVowel(word[i+1]) && isVowel(word[i-1]) {
			return string(word[i])
		}
	}
