// Write your code here
}

Solution:
```go
func Solve(s string) string {
    result := ""
    isLetter := false
    for _, c := range s {
        if c >= 'a' && c <= 'z' || c >= 'A' && c <= 'Z' {
            isLetter = true
            if c >= 'a' && c <= 'z' {
                result += string(c - 32)
            } else {
                result += string(c + 32)
            }
        } else {
            if isLetter {
                result += string(c)
            } else {
                result = string(c) + result
            }
            isLetter = false
        }
    }
    if !isLetter {
        result = reverse(result)
    }
    return result
}

func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}
```
Explanation:

The problem can be broken down into two parts: reversing the case of letters and reversing the string if it contains no letters.

We iterate through each character in the string. If the character is a letter, we reverse its case and add it to the result string. If the character is not a letter, we add it to the result string only if we have seen a letter before (i.e., `isLetter` is `true`). We then reset `isLetter` to `false`.

After iterating through the entire string, we check if `isLetter` is still `false`. If it is, it means the string contains no letters, so we reverse the result string using the `reverse` function.

The `reverse` function is a simple implementation of string reversal. It uses a slice of runes to store the characters of the string and then swaps the characters at the beginning and end of the slice, moving towards the center. Finally, it converts the slice of runes back to a string and returns it.