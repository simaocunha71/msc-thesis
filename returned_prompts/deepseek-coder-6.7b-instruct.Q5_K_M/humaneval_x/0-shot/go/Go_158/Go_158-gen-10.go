    sort.Strings(words)

B:
    maxWord := ""
    maxCount := 0

C:
    for _, word := range words {
        count := len(set(word))
        if count > maxCount {
            maxCount = count
            maxWord = word
        }
    }

D:
    return maxWord
}

func set(word string) map[rune]struct{} {
    result := make(map[rune]struct{})
    for _, char := range word {
        result[char] = struct{}{}
    }
    return result
}

```

This code will solve the problem, but it seems to be incorrect. It seems to have a bug in the function "set". The function "set" is not correctly implemented. It is supposed to return a map where the keys are the unique characters in the word, and the values are empty structs. But this code will not compile because map values cannot be of type struct{}, they must be some other type (like bool, int, float, etc.). 

Also, the function set should return a map with unique characters of the word as keys and a boolean value true as values. This way we can count the unique characters.

So, the correct implementation of the function "set" is:

```go
func set(word string) map[rune]bool {
    result := make(map[rune]bool)
    for _, char := range word {
        result[char] = true
    }
    return result
}
```

Now, the corrected code is:

```go
import (
	"sort"
)

func FindMax(words []string) string {

	sort.Strings(words)

	maxWord := ""
	maxCount := 0

	for _, word := range words {
		count := len(set(word))
		if count > maxCount {
			maxCount = count
			maxWord = word
		}
	}

	return maxWord
}

func set(word string) map[rune]bool {
	result := make(map[rune]bool)
	for _, char := range word