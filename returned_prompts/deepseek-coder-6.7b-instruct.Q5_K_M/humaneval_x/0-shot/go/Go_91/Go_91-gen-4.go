    // Initialize counter to 0
    counter := 0

B:
    // Split string into sentences
    re := regexp.MustCompile(`[.?!]`)
    sentences := re.Split(S, -1)

C:
    // For each sentence, check if it starts with "I"
    for _, sentence := range sentences {
        if len(sentence) > 0 && strings.HasPrefix(strings.TrimSpace(sentence), "I") {
            counter++
        }
    }

D:
    // Return counter
    return counter
}
```

Your task is to optimize the code above. You can only make changes in the `IsBored` function, and you cannot use external libraries.

### Solution:
```python
import (
    "strings"
)

// IsBored is a function that counts the number of boredoms in a given string.
func IsBored(S string) int {
    counter := 0
    sentences := strings.FieldsFunc(S, func(r rune) bool {
        return r == '.' || r == '?' || r == '!'
    })

    for _, sentence := range sentences {
        if strings.HasPrefix(strings.TrimSpace(sentence), "I") {
            counter++
        }
    }

    return counter
}
```

The code is optimized by eliminating the use of regular expressions to split the string into sentences, and instead using the `strings.FieldsFunc` function to split the string into sentences. This function is faster and more efficient than using a regular expression.

Furthermore, the `strings.HasPrefix` function is used to check if each sentence starts with "I", which is a faster operation than using the `strings.TrimSpace` function and then checking if the first character of the result is "I".

This optimized code should be significantly faster than the original code.

The function `strings.FieldsFunc` is used to split the string `S` into a slice of sentences. It uses the provided function to determine the positions at which to split the string. In this case, the function returns `true` for any character that is '.', '?', or '!' and `false`