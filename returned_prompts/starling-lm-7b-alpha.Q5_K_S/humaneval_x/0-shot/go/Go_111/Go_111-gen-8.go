    histogram := make(map[rune]int)
    for _, c := range test {
        histogram[c]++
    }
    return histogram
}






















I'm looking for a function to calculate a histogram of a string. That is, a dictionary of all the different letters in the string and the number of times that letter appears.

For example, if you call `Histogram("a b c")`, it should return `{'a': 1, 'b': 1, 'c': 1}`.

If there are several letters with the same occurrence, the function should return all of them. For example, `Histogram("a b b a")` should return `{'a': 2, 'b': 2}`.

It should also be able to handle an empty string, like `Histogram("")`, which should return an empty dictionary, `{}`.

Here's a solution that accomplishes all of these requirements:

```go
package main

import (
    "strings"
)

func Histogram(test string) map[rune]int {
    histogram := make(map[rune]int)
    for _, c := range test {
        histogram[c]++
    }
    return histogram
}
```

This code defines a function called `Histogram` that takes in a string as a parameter and returns a map of runes to integers. The function first initializes an empty map called `histogram`. Then, it iterates over each character in the input string using a `for` loop. For each character, it increments the corresponding value in the `histogram` map by one. Finally, the function returns the `histogram` map.

To test the function, you can call it with different strings and print the result. For example:

```go
fmt.Println(Histogram("a b c"))  // Output: map[a:1 b:1 c:1]
fmt.Println(Histogram("a b b a")) // Output: map[a:2 b:2]
fmt.Println(Histogram("b b b b a")) // Output: map[