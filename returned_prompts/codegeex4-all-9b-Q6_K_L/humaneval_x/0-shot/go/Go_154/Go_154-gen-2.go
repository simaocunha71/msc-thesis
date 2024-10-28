You can solve this problem by checking if the second word is a substring of the first word, and also checking if any rotation of the second word is a substring of the first word. Here is a possible implementation in Go:

```go
func CycpatternCheck(a, b string) bool {
    // Check if b is a substring of a
    if strings.Contains(a, b) {
        return true
    }

    // Check if any rotation of b is a substring of a
    for i := 1; i < len(b); i++ {
        rotated := b[i:] + b[:i]
        if strings.Contains(a, rotated) {
            return true
        }
    }

    return false
}
```

This implementation first checks if `b` is a substring of `a`. If it is, then it returns `true`. Otherwise, it checks if any rotation of `b` is a substring of `a`. If it is, then it returns `true`. If neither of these conditions are met, then it returns `false`.

This implementation uses the `strings.Contains` function to check if one string is a substring of another string. It also uses a for loop to generate the rotations of `b`.