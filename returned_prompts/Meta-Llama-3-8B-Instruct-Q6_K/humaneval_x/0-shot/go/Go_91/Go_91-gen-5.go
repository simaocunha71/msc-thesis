```go
package main

import (
	"regexp"
)

func IsBored(S string) int {
	// Use a regular expression to find all sentences that start with "I"
	re, _ := regexp.Compile(`^[Ii].*?[.!?]`)
	return len(re.FindAllString(S, -1))
}
```

Explanation:
The regular expression `^[Ii].*?[.!?]` matches any sentence that starts with either "I" or "i" (to make the regular expression case-insensitive), followed by any characters (including none) until a period, question mark, or exclamation mark is found. This pattern is anchored to the start of the string (`^`) and the end of the sentence (`.*?` is a lazy match).

The `FindAllString` function is used to find all matches of the regular expression in the input string `S`. The `-1` at the end of the function call means that it should find all matches, not just the first one.

The length of the resulting slice of strings is returned as the number of boredoms.