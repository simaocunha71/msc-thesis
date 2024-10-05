    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        newRunes = append(newRunes, (ch-5+'z'-'a'+1)%26+'a')
    }
    return string(newRunes)
}

// Returns an encoded string by shifting every character by 5 in the alphabet.
func EncodeShift(s string) string {
    var encoded string
    for _, r := range s {
        encoded += string((r + 5) % 26 + 'a')
    }
    return encoded
}

// Returns the original string by shifting the encoded string back by 5 in the alphabet.
func DecodeShift(s string) string {
    var decoded string
    for _, r := range s {
        decoded += string((r - 5) % 26 + 'a')
    }
    return decoded
}

As we can see, the EncodeShift function takes a string as an input and returns an encoded string by shifting every character by 5 in the alphabet. The DecodeShift function takes as input a string encoded with the EncodeShift function and returns the decoded string.

In the first solution, the EncodeShift function uses a for loop to iterate over each character in the input string. It appends the shifted character to a new slice of runes. The shifted character is calculated by adding 5 to the character's Unicode value and taking the modulo 26. The resulting shifted character is then converted back to a string and appended to the newRunes slice. Finally, the EncodeShift function returns the encoded string.

The DecodeShift function works in a similar way. It iterates over each character in the input string, subtracts 5 from the character's Unicode value, and takes the modulo 26. The resulting shifted character is then converted back to a string and appended to the newRunes slice. The DecodeShift function returns the decoded string.

In the second solution, the EncodeShift function uses a for loop to iterate over each rune in the input string. It converts the rune to a string and appends it to the encoded string.