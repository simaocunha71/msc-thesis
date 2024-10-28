Here is a possible solution in Go:
```go
package main

import (
    "strings"
)

func ReverseDelete(s, c string) [2]interface{} {
    // Remove all characters in s that are equal to any character in c
    result := strings.Map(func(r rune) rune {
        for _, c := range c {
            if r == c {
                return -1
            }
        }
        return r
    }, s)

    // Convert the result to a string
    resultStr := string(result)

    // Check if the result string is palindrome
    isPalindrome := strings.EqualFold(resultStr, strings.Reverse(resultStr))

    // Return a tuple containing the result string and the check result
    return [2]interface{}{resultStr, isPalindrome}
}

func main() {
    s := "abcdedcba"
    c := "ab"
    result, _ := ReverseDelete(s, c)
    println(result)  // Output: ["cdedc", true]
}
```
This solution uses the `strings.Map` function to remove all characters in `s` that are equal to any character in `c`. It then converts the result to a string and checks if it's a palindrome using the `strings.EqualFold` and `strings.Reverse` functions. Finally, it returns a tuple containing the result string and the check result.

Note that the `strings.Map` function returns a `string` type, so we need to convert the result to a string using the `string` function. Also, the `strings.EqualFold` function is used to check if the result string is a palindrome, ignoring the case of the characters. If you want to check the palindrome property with case sensitivity, you can use the `strings.EqualFold` function with the `strings.ToLower` function. For example:
```go
isPalindrome := strings.EqualFold(strings.ToLower(resultStr), strings.Reverse(strings.ToLower(resultStr)))
``` A tuple is a collection of items that are stored in a single variable. In Go, a tuple is a value of type `[2]interface{}`. In the code above, we are creating a tuple with two elements: the result string and the check result. The `println` function is used to print the result. If you want to return a tuple from a function, you can use the following syntax: `return [2]interface{}{resultStr, isPalindrome}`. This will return a tuple with two elements: the result string and the check result. A tuple is a