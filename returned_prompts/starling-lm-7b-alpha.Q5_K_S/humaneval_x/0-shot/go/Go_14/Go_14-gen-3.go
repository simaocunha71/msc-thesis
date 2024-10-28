
To solve this problem, we can iterate through the string and append each substring to a slice. The substrings should be sorted in ascending order by length. Here's one way to do it:

```go
func AllPrefixes(str string) []string {
    prefixes := []string{}
    for i := 0; i < len(str); i++ {
        prefixes = append(prefixes, str[:i+1])
    }
    return prefixes
}
```

In this solution, we use a slice called `prefixes` to store the prefixes of the string. We start by initializing it as an empty slice. Then, we iterate through the indices of the string using a `for` loop. For each index `i`, we append the substring from index 0 to `i+1` to the `prefixes` slice using the `append` function. This way, we add all the prefixes of the string to the slice.

Finally, we return the `prefixes` slice, which contains all the prefixes of the input string in ascending order of length.

You can test this solution with the provided example:

```go
package main

import "fmt"

func main() {
    fmt.Println(AllPrefixes("abc"))
}
```

This will output `['a', 'ab', 'abc']`, which are all the prefixes of the string "abc" in ascending order of length.

```go
package main

import "fmt"

func main() {
    fmt.Println(AllPrefixes("abc"))
}
```

This will output `['a', 'ab', 'abc']`, which are all the prefixes of the string "abc" in ascending order of length.

```

```

```go
package main

import "fmt"

func main() {
    fmt.Println(AllPrefixes("abc"))
}
```

This will output `['a', 'ab', 'abc']`, which are all the prefixes of the string "abc" in ascending order of length.

```

```

```go
package main

import "fmt"
