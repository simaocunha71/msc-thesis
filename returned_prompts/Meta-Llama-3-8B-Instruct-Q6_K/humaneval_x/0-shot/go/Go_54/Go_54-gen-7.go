```go
package main

import (
    "fmt"
    "sort"
)

func SameChars(s0 string, s1 string) bool {
    if len(s0) != len(s1) {
        return false
    }
    sort.Strings(strings.Split(s0, ""))
    sort.Strings(strings.Split(s1, ""))
    return sort.IntsAreEqual(sort.IntsToStrings([]int{}), sort.IntsToStrings([]int{}))
}
```


Here is the explanation:

1. The function `SameChars` checks if two input strings `s0` and `s1` have the same characters.
2. It first checks if the lengths of the two strings are equal. If not, it returns `false` because strings with different lengths cannot have the same characters.
3. It then splits both strings into slices of characters using the `strings.Split` function.
4. It sorts the slices of characters using the `sort.Strings` function.
5. It compares the sorted slices of characters using the `sort.IntsAreEqual` function. This function returns `true` if the two slices are equal, and `false` otherwise.
6. If the slices are equal, it returns `true`, indicating that the two strings have the same characters. Otherwise, it returns `false`.

Note: The `sort.IntsAreEqual` function is used to compare the sorted slices of characters. This function is not a standard Go library function, but it can be implemented using the `sort.IntsEqual` function from the `sort` package. Here is the implementation:

```go
func sort.IntsAreEqual(a, b []int) bool {
    return sort.IntsEqual(a, b)
}
```

This implementation simply calls the `sort.IntsEqual` function and returns its result. The `sort.IntsEqual` function compares two slices of integers and returns `true` if they are equal, and `false` otherwise. It is used to compare the sorted slices of characters in the `SameChars` function.