
// This function is used to check if a given string b is a rotation of a given string a

// First, we concatenate string a with itself. This doubles the length of string a.
// Then we check if string b is a substring of the resultant string.
// If it is, then b is a rotation of a.

	ab := a + a
	if strings.Contains(ab, b) {
		return true
	}
	return false
}
```

## 2. Solution 2

```go
