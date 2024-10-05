```go
package main
import "strings"

func IsPalindrome(text string) bool {
    text = strings.ToLower(text) // convert to lowercase
    text = strings.ReplaceAll(text, " ", "") // remove spaces
    text = strings.ReplaceAll(text, ",", "") // remove commas
    text = strings.ReplaceAll(text, ".", "") // remove dots
    text = strings.ReplaceAll(text, "-", "") // remove hyphens
    text = strings.ReplaceAll(text, "'", "") // remove single quotes
    text = strings.ReplaceAll(text, "\"", "") // remove double quotes

    // reverse the string
    for left, right := 0, len(text)-1; left < right; left, right = left+1, right-1 {
        text = text[:left] + string(text[right]) + text[left+1:right] + text[left:right]
    }

    // check if the string is equal to its reverse
    return text == reverse(text)
}

func reverse(text string) string {
    runes := []rune(text)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}
```

Explanation:

This code checks if a given string is a palindrome. A palindrome is a string that reads the same backward as forward.

The code first converts the string to lowercase and removes all non-alphanumeric characters (spaces, commas, dots, hyphens, single quotes, and double quotes) to ensure the comparison is case-insensitive and ignores special characters.

Then, it reverses the string by swapping characters from the beginning and end of the string, moving towards the center.

Finally, it checks if the original string is equal to its reversed version. If they are equal, the string is a palindrome and the function returns true; otherwise, it returns false.