To solve this problem, we can follow these steps:

1. Replace all spaces in the string with underscores.
2. Replace all consecutive spaces with a dash.
3. Return the modified string.

Here is a solution in Go:
```go
func FixSpaces(text string) string {
	var i int = 0
	var j int = 0
	var n int = len(text)
	var spaces int = 0
	var result string = ""
	
	for i < n {
		if text[i] == ' ' {
			spaces++
		} else {
			if spaces > 0 {
				if spaces > 2 {
					result += "-"
				} else {
					result += "_"
				}
				spaces = 0
			}
			j = i + 1
			for j < n && text[j] != ' ' {
				result += string(text[j])
				j++
			}
			if j < n {
				result += "_"
			}
			i = j
		}
		i++
	}
	
	if spaces > 0 {
		if spaces > 2 {
			result += "-"
		} else {
			result += "_"
		}
	}
	return result
}
```

This solution uses two pointers `i` and `j` to traverse the string, and a variable `spaces` to keep track of the number of consecutive spaces. It also uses a variable `result` to store the modified string.

The algorithm works as follows:

- Initialize `i` to 0 and `j` to 0, and set `n` to the length of the input string.
- Iterate through the string using `i` as the index.
- If the character at index `i` is a space, increment the `spaces` variable.
- If the character at index `i` is not a space, check if