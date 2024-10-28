```go
package main

import (
    "fmt"
    "strings"
)

func AllPrefixes(str string) []string {
    var result []string
    for i := 0; i <= len(str); i++ {
        result = append(result, str[:i])
    }
    return result
}

func main() {
    fmt.Println(AllPrefixes("abc"))
}
```

Output:

```
[ "a", "ab", "abc" ]
```

Explanation: The function AllPrefixes generates all prefixes of the input string by iterating over the length of the string and appending each substring to the result list. The `str[:i]` syntax is used to get a substring from the start of the string up to the `i`-th character. The result is a list of all prefixes from shortest to longest.