```go
package main

import (
    "fmt"
    "strings"
)

func AllPrefixes(str string) []string {
    prefixes := make([]string, 0)
    for i := 0; i <= len(str); i++ {
        prefixes = append(prefixes, str[:i])
    }
    return prefixes
}

func main() {
    fmt.Println(AllPrefixes("abc"))
}
```

S:
```go
package main

import (
    "fmt"
    "strings"
)

func AllPrefixes(str string) []string {
    return strings.Split(str, "")
}

func main() {
    fmt.Println(AllPrefixes("abc"))
}
```

Explanation:
The problem asks for a function that takes a string as input and returns a list of all its prefixes from shortest to longest. The prefixes are the substrings of the input string that appear at the beginning of the string.

The first solution uses a loop to generate all prefixes of the input string. It starts by initializing an empty slice `prefixes`. Then, it iterates over the length of the input string, and for each iteration, it appends a substring of the input string from the beginning to the current position to the `prefixes` slice. Finally, it returns the `prefixes` slice.

The second solution uses the `strings.Split` function to split the input string into its individual characters, which are the prefixes of the input string. The `strings.Split` function splits a string into substrings separated by a specified separator. In this case, the separator is an empty string, which means that the function will split the input string into its individual characters. The function then returns the resulting slice of prefixes.