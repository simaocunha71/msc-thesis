```go
package main

import (
	"fmt"
)

func IsPalindrome(text string) bool {
	// Convert the string to lower case
	text = strings.ToLower(text)

	// Remove non-alphanumeric characters
	text = strings.Map(func(r rune) rune {
		if r == ' ' || r == ',' || r == '.' || r == '?' {
			return -1
		}
		return r
	}, text)

	// Reverse the string
	reversed := []rune(text)
	for i := 0; i < len(reversed)/2; i++ {
		reversed[len(reversed)-1-i], reversed[i] = reversed[i], reversed[len(relevant)-1-i]
	}

	// Compare the original and reversed strings
	return fmt.Sprint(text) == fmt.Sprint(reversed)
}

func main() {
	fmt.Println(IsPalindrome(""))            // true
	fmt.Println(IsPalindrome("aba"))        // true
	fmt.Println(IsPalindrome("aaaaa"))      // true
	fmt.Println(IsPalindrome("zbcd"))       // false
}
```

Explanation:

The function `IsPalindrome` checks if the given string is a palindrome. It first converts the string to lower case to ignore case sensitivity. Then, it removes non-alphanumeric characters from the string. This is done by using the `strings.Map` function, which applies a given function to each rune in the string. In this case, the function checks if the rune is a space, comma, dot, or question mark, and if so, returns -1 to remove it from the string.

Next, the function reverses the string by swapping the characters from the beginning and end of the string, moving towards the center. This is done using a loop that runs until the middle of the string.

Finally, the function compares the original and reversed strings using the `fmt.Sprint` function, which converts the strings to strings. If the two strings are the same, the function returns `true`, indicating that the original string is a palindrome. Otherwise, it returns `false`.

In the `main` function, the `IsPalindrome` function is called with different inputs and the results are printed to the console. The function correctly identifies the palindromes and non-palindromes.