```go
package kata

import "unicode"

func Solve(s string) string {
    var letters []rune
    for _, c := range s {
        if unicode.IsLetter(c) {
            letters = append(letters, unicode.ToLower(c))
        } else {
            letters = append(letters, c)
        }
    }
    if len(letters) > 0 {
        for i := 0; i < len(letters)/2; i++ {
            letters[i], letters[len(letters)-i-1] = letters[len(letters)-i-1], letters[i]
        }
    } else {
        for i := 0; i < len(s)/2; i++ {
            s = s[:i] + string(s[len(s)-i-1]) + s[i+1:]
        }
    }
    return string(letters)
}
```
