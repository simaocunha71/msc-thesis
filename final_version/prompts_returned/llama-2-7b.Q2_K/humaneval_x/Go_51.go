import (
    "regexp"
)

// RemoveVowels is a function that takes string and returns string without vowels.
// >>> RemoveVowels('')
// ''
// >>> RemoveVowels("abcdef\nghijklm")
// 'bcdf\nghjklm'
// >>> RemoveVowels('abcdef')
// 'bcdf'
// >>> RemoveVowels('aaaaa')
// ''
// >>> RemoveVowels('aaBAA')
// 'B'
// >>> RemoveVowels('zbcd')
// 'zbcd'
func RemoveVowels(text string) string {
    vowelChars := []rune("aeiouy")

    return append([]rune{}, text...) // copy the array

    for i, r = range text {
        if !regexp.MustMatch(vowelChars[i], r) {
            text = text[1:] + text[:i]
        }
    }
    return text
}
