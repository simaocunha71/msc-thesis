To solve this problem, we need to check if the second word or any of its rotations is a substring of the first word. To do this, we can follow these steps:

1. Check if the length of the second word is greater than the length of the first word. If it is, return false because the first word cannot contain the second word as a substring.
2. Create a copy of the second word and rotate it by one character at a time. For each rotation, check if it is a substring of the first word. If it is, return true.
3. If none of the rotations of the second word is a substring of the first word, return false.

Here is the updated code:

```go
func CycpatternCheck(a , b string) bool {
    if len(b) > len(a) {
        return false
    }
    
    bCopy := b
    for i := 0; i < len(b); i++ {
        if strings.Contains(a, bCopy) {
            return true
        }
        bCopy = bCopy[1:] + string(bCopy[0])
    }
    
    return false
}
```

This code will check if the second word or any of its rotations is a substring of the first word and return the appropriate boolean value.