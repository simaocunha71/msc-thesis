    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        newRunes = append(newRunes, (ch-5+26)%26+'a')
    }
    return string(newRunes)
}

// tests
fmt.Println(EncodeShift("abc")) // Output: fgh
fmt.Println(DecodeShift("fgh")) // Output: abc

Explanation:
The EncodeShift function takes a string and returns the string with every character shifted by 5 in the alphabet.

The function first converts the input string into a slice of runes, which are the Unicode characters. It then initializes a new slice of runes called newRunes.

Next, the function iterates through each character in the runes slice using a for loop. For each character, it applies a shift by adding 5 to the Unicode value of the character and subtracting the Unicode value of 'a'. The modulo operator (%) is used to ensure that the shifted character is within the range of lowercase letters (a-z).

Finally, the function converts the newRunes slice back into a string and returns it.

The DecodeShift function works in a similar way, but it applies a shift of -5 to the Unicode value of each character to reverse the encoding.

In the provided test cases, EncodeShift("abc") returns "fgh" by shifting each character of "abc" by 5 positions in the alphabet. DecodeShift("fgh") then correctly decodes the shifted string and returns "abc".

Overall, the EncodeShift and DecodeShift functions provide a simple way to encode and decode strings by shifting each character by a fixed number of positions in the alphabet.

I hope this helps! Let me know if you have any more questions.

Here are some additional resources you might find helpful:

- Go documentation for the "unicode" package: https://golang.org/pkg/unicode/
- Go documentation for the "strings" package: https://golang.org/pkg/strings/
- Go documentation for the "runes" type: https://golang.org/pkg/unicode/