```go
package main

import (
	"fmt"
	"strings"
)

func IsPalindrome(text string) bool {
	text = strings.ToLower(text)
	reverse := ""
	for i := len(text) - 1; i >= 0; i-- {
		reverse += string(text[i])
	}
	return text == reverse
}

func main() {
	fmt.Println(IsPalindrome(""))       // true
	fmt.Println(IsPalindrome("aba"))    // true
	fmt.Println(IsPalindrome("aaaaa"))  // true
	fmt.Println(IsPalindrome("zbcd"))   // false
}
```
Output:
```
true
true
true
false
```

Explanation:
The function `IsPalindrome` checks whether a given string is a palindrome. It converts the input string to lowercase, reverses it, and then compares it with the original string. If the reversed string is the same as the original string, the function returns `true`, indicating that the string is a palindrome. Otherwise, it returns `false`.

The function uses the `strings.ToLower` function to convert the input string to lowercase, ensuring that the comparison is case-insensitive. It then uses a loop to reverse the string by concatenating the characters in reverse order. Finally, it compares the reversed string with the original string using the `==` operator.

In the `main` function, we test the `IsPalindrome` function with different input strings and print the results. The output shows that the function correctly identifies palindromes and non-palindromes.