    var result string
    vowels := map[rune]rune{'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w', 'A': 'C', 'E': 'G', 'I': 'K', 'O':': 'Q', 'U': 'W'}

    for _, char := range message {
        switch {
        case strings.ContainsRune("aeiouAEIOU", char):
            result += string(vowels[char])
        default:
            result += string(char)
        }
    }

    return result
}

This function works by first creating a map with the vowels and their replacements. Then it loops through each character in the input message. If the character is a vowel, it adds the replacement vowel to the result string. If it's not a vowel, it just adds the original character.

This function uses the built-in strings.ContainsRune function to check if a character is a vowel.

Finally, it returns the result string, which is the encoded message.

Note: In the map 'vowels', lowercase vowels are mapped to uppercase vowels, as specified in the problem statement.

This function assumes that the input message only contains letters and spaces. If the input message contains any other characters, the function may not work correctly.

Also, the function uses the built-in strings.ContainsRune function to check if a character is a vowel. This function is not efficient for large inputs, as it has to search the entire string for each character. A more efficient approach would be to create a set of vowels and check if a character is in the set. However, Go does not have a built-in set data structure, so we use the strings.ContainsRune function instead.

The time complexity of this function is O(n), where n is the length of the input message. This is because we loop through each character in the message once. The space complexity is also O(n), because we create a new string that is the same length as the input message.

Test this function with the given examples and ensure it works as expected.

For example:

fmt.Println(Encode("test")) // outputs: