You can use the following code to check if two words have the same characters:

```
func SameChars(s0 string, s1 string) bool {
    if len(s0) != len(s1) {
        return false
    }
    for i := 0; i < len(s0); i++ {
        if !strings.Contains(s1, string(s0[i])) {
            return false
        }
    }
    return true
}
```

This code first checks if the lengths of the two strings are the same. If not, it returns false. Then it iterates over each character in the first string and checks if that character is in the second string using the `strings.Contains` function. If any character is not in the second string, it returns false. If all characters are in the second string, it returns true.