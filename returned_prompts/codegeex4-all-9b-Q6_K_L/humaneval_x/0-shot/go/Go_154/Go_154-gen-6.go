The cyclical pattern problem is a common problem in computer science and mathematics. The idea is to check if a string is a substring of another string. In this case, the second string is a rotation of the first string.

To solve this problem, we can use the following steps:

1. Create a new string by concatenating the first string with itself. This will allow us to handle cases where the second string is a rotation of the first string but not a substring.
2. Check if the second string is a substring of the new string.
3. If the second string is a substring, return true. Otherwise, return false.

Here is the implementation of the function in Go:

```
func CycpatternCheck(a , b string) bool {
    s := a + a
    return strings.Contains(s, b)
}
```

This function takes two strings as input and returns a boolean value. The function creates a new string by concatenating the first string with itself. It then checks if the second string is a substring of the new string using the `strings.Contains` function. If the second string is a substring, the function returns true. Otherwise, it returns false.