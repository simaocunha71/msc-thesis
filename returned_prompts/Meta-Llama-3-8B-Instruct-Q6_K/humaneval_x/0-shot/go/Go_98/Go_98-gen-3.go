Here is a simple solution in Go:

```go
import (
    "strings"
)

func CountUpper(s string) int {
    count := 0
    for i, c := range s {
        if i%2 == 0 && strings.ToUpper(string(c)) == string(c) {
            count++
        }
    }
    return count
}
```

This function iterates over the input string `s`. For each character, it checks if the index `i` is even (`i%2 == 0`) and if the character is uppercase (`strings.ToUpper(string(c)) == string(c)`). If both conditions are true, it increments the `count` variable. Finally, it returns the `count`.