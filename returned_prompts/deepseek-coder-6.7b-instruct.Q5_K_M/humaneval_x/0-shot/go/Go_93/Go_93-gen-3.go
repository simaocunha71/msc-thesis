    encoded := ""
    for _, c := range message {
        if strings.ContainsRune("aeiou", unicode.ToLower(c)) {
            switch unicode.ToLower(c) {
            case 'a':
                encoded += "C"
            case 'e':
                encoded += "G"
            case 'i':
                encoded += "K"
            case 'o':
                encoded += "Q"
            case 'u':
                encoded += "W"
            }
        } else {
            switch c {
            case 'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u':
                continue A
            }
            encoded += strings.ToUpper(string(c))
        }
    }
    return encoded
}

This function encodes the input message by swapping case of all letters and replacing all vowels with the letter that appears 2 places ahead of that vowel in the english alphabet. The result is the encoded message.

The function starts by initializing an empty string encoded. Then it iterates over each character in the input message. If the character is a vowel (checked using strings.ContainsRune and unicode.ToLower), it replaces the vowel with the corresponding character in the english alphabet that appears 2 places ahead. If the character is not a vowel, it adds the character to the encoded string unchanged. Finally, the function returns the encoded string.

Please note that this function assumes that the input message only contains letters and spaces. If the input message contains other characters, the function may not behave as expected.
*/
package main

import (
	"fmt"
)

func Encode(message string) string {
	encoded := ""
	for _, c := range message {
		switch c {
		case 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U':
			c += 2
		case 'z':
			c = 'b'
		case 'Z':
			c = 'B'
		}
		encoded += string(c)
	}
	return encoded
}

func main() {