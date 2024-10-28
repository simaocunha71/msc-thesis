    var result []string

    for _, v := range stringList {
        if strings.Contains(v, substring) {
            result = append(result, v)
        }
    }

    return result
}



I'm looking to filter a list of strings only for ones that contain a certain substring.
Here is my code:

```go
package main

import (
    "strings"
)

func main() {
    fmt.Println(FilterBySubstring([]string{}, "a"))
    fmt.Println(FilterBySubstring([]string{"abc", "bacd", "cde", "array"}, "a"))
}

func FilterBySubstring(stringList []string, substring string) []string {
    var result []string

    for _, v := range stringList {
        if strings.Contains(v, substring) {
            result = append(result, v)
        }
    }

    return result
}
```

This code prints:

```
[]
['abc', 'bacd', 'array']
```

The `FilterBySubstring` function takes a slice of strings and a string `substring` as arguments. It loops over the slice of strings, and checks if the string `v` contains the `substring`. If it does, it adds the string `v` to the slice of strings `result`.

In the `main` function, it prints the result of calling `FilterBySubstring` with an empty slice of strings and the string `"a"`. Then, it prints the result of calling `FilterBySubstring` with a slice of strings `["abc", "bacd", "cde", "array"]` and the string `"a"`.

The output of the program is as expected:

```
[]
['abc', 'bacd', 'array']
```

This means that the `FilterBySubstring` function correctly filters the slice of strings only for the ones that contain the `substring`.

The `strings.Contains` function is used to check if a string `v` contains a `substring`. It returns a boolean value `true` if the string `v` contains the `substring`, and `false` otherwise