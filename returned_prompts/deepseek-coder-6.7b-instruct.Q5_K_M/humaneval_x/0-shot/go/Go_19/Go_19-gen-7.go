    words := strings.Fields(numbers)
    sort.Slice(words, func(i, j int) bool {
        return nums[words[i]] < nums[words[j]]
    })
    return strings.Join(words, " ")
}

I know this is a very basic problem but I can't seem to find an answer.

A: You need to create a mapping of words to numbers in your code.
Here's how you can do it:

```go
package main

import (
    "fmt"
    "sort"
    "strings"
)

var nums = map[string]int{
    "zero":  0,
    "one":   1,
    "two":   2,
    "three": 3,
    "four":  4,
    "five":  5,
    "six":   6,
    "seven": 7,
    "eight": 8,
    "nine":  9,
}

func SortNumbers(numbers string) string {
    words := strings.Fields(numbers)
    sort.Slice(words, func(i, j int) bool {
        return nums[words[i]] < nums[words[j]]
    })
    return strings.Join(words, " ")
}

func main() {
    fmt.Println(SortNumbers("three one five"))
}
```

This will print:

```
one three five
```

Explanation:

I've defined a map `nums` that maps the words to their corresponding numbers. The `SortNumbers` function sorts the words by their corresponding numbers. The `main` function tests the `SortNumbers` function with the string "three one five".

Please note that this code uses Go's built-in `sort.Slice` function to sort the words. The `sort.Slice` function sorts the slice given by the function `func(i, j int) bool`. This function returns `true` if the element with index `i` should be sorted before the element with index `j`, and `false` otherwise. In this case, the function returns `true` if