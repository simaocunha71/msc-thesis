Here is the solution in Go:
```go
import (
    "strings"
)

func ReverseDelete(s, c string) [2]interface{} {
    // Create a new string by removing all characters in s that are equal to any character in c
    newS := strings.Map(func(r rune) rune {
        if strings.ContainsRune(c, r) {
            return -1
        }
        return r
    }, s)

    // Convert the new string to lowercase to ignore case sensitivity
    newS = strings.ToLower(newS)

    // Check if the new string is a palindrome
    isPalindrome := strings.EqualFold(newS, reverse(newS))

    // Return the new string and the result of the palindrome check
    return [2]interface{}{newS, isPalindrome}
}

// Function to reverse a string
func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}
```
Here's an explanation of the code:

1. We use the `strings.Map` function to create a new string by removing all characters in `s` that are equal to any character in `c`. We do this by using a lambda function that returns -1 if the character is found in `c`, and the original character otherwise.
2. We convert the new string to lowercase using the `strings.ToLower` function to ignore case sensitivity.
3. We check if the new string is a palindrome using the `strings.EqualFold` function, which ignores case sensitivity. We pass the new string and its reverse as arguments.
4. We return a tuple containing the new string and the result of the palindrome check.

The `reverse` function is a simple implementation of a string reversal algorithm. It uses a slice of runes (the underlying type of strings in Go) to reverse the string in place.

You can test this function with the examples you provided to see that it returns the expected results. For example:
```go
s, c := "abcde", "ae"
result := ReverseDelete(s, c)
fmt.Println(result) // Output: ['bcd' false]

s, c = "abcdef", "b"
result = ReverseDelete(s, c)
fmt.Println(result) // Output: ['acdef' false]

s, c