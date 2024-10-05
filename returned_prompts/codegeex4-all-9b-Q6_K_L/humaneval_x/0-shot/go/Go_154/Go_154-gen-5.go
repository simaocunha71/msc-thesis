```go
func CycpatternCheck(a , b string) bool {
	for i := 0; i < len(b); i++ {
		if strings.Contains(a, b[i:]) && strings.Contains(a, b[:i]) {
			return true
		}
	}
	return false
}
```
This solution works by checking if the second word or any of its rotations is a substring of the first word. It does this by iterating through the second word and checking if the substring starting from the current position and ending at the end of the word, as well as the substring starting from the beginning of the word and ending at the current position, are both substrings of the first word. If either of these conditions is true, it returns true. If none of these conditions are true after iterating through the entire second word, it returns false.