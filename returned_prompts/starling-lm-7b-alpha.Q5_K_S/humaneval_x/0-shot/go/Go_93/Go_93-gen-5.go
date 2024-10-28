    const vowel = "AEIOU"
    const vowelMap = map[rune]rune{
        'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w',
    }

    message = strings.ToLower(message)
    v := []rune(message)
    for i, c := range v {
        if strings.ContainsRune(vowel, c) {
            v[i] = vowelMap[c]
        } else {
            v[i] = v[i] ^ rune('A' - 'a') ^ rune('a' - 'A')
        }
    }
    return string(v)
}








I have a function that takes a message as a string and encodes it.
The encoding of the message swaps the case of all letters. For example, lower case letters are converted to upper case and vice versa.
The encoding also replaces all vowels in the message with the letter that appears two places ahead of that vowel in the English alphabet. For example, if the vowel is "a", it will be replaced by "c".

The function should return the encoded message as a string.

Explanation:

The function first creates a constant string variable called "vowel" containing the vowels "AEIOU".
Then it creates a constant string variable called "vowelMap" which maps each vowel to the letter that appears two places ahead of it in the English alphabet. For example, "a" is mapped to "c", "e" is mapped to "g", "i" is mapped to "k", "o" is mapped to "q", and "u" is mapped to "w".

The function then converts the input message to lowercase using the "strings.ToLower" function and stores it in the variable "v".
Next, it iterates over each character in the "v" variable using a for loop. For each character, it checks if it is a vowel using the "strings.ContainsRune" function. If the character is a vowel, it replaces it with the corresponding letter from the "vowelMap