
// Check if the string is empty
if len(text) == 0 {
return true
}

// Remove all non-alphanumeric characters from the string
text = strings.Map(func(r rune) rune {
if unicode.IsLetter(r) || unicode.IsDigit(r) {
return r
}
return -1
}, text)

// If the string length is even, make sure the middle character is the same
if len(text) % 2 == 0 {
return text == text[0:len(text)/2] == text[len(text)/2+1:]
}

// If the string length is odd, make sure the first and last characters are the same
return text == text[0] == text[len(text)-1] && text[0:len(text)/2] == text[len(text)/2+1:]
}

Explanation:
The function IsPalindrome takes a string as input and returns a boolean value indicating whether the string is a palindrome or not.

The function first checks if the input string is empty. If it is, the function returns true because an empty string can be considered a palindrome.

Next, the function removes all non-alphanumeric characters from the string using the strings.Map function. This ensures that the function only compares alphanumeric characters when checking for palindromes.

Then, the function checks if the length of the string is even. If it is, the function compares the first half of the string (from index 0 to len(text)/2) with the second half of the string (from index len(text)/2+1 to the end). If they are the same, the function returns true.

If the length of the string is odd, the function compares the first character of the string with the last character, and the first half of the string with the second half (excluding the first and last characters). If both comparisons are true, the function returns true.

Overall, this function provides a comprehensive solution to check if a given string is a palindrome, taking into account both even and odd-length strings, as well as alphanumeric characters only.

// Checks if given string is a palindrome
