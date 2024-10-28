Here is a simple Go function that filters a list of strings to only include those that contain a given substring:
```go
import (
    "strings"
)

func FilterBySubstring(stringList []string, substring string) []string {
    var result []string
    for _, str := range stringList {
        if strings.Contains(str, substring) {
            result = append(result, str)
        }
    }
    return result
}
```
Here's an explanation of the code:

* We import the `strings` package, which provides functions for working with strings.
* The `FilterBySubstring` function takes two inputs: `stringList`, a slice of strings, and `substring`, a string.
* We initialize an empty slice `result` to store the filtered strings.
* We iterate over the input `stringList` using a `for` loop.
* For each string `str` in the list, we use the `strings.Contains` function to check if it contains the given `substring`. If it does,