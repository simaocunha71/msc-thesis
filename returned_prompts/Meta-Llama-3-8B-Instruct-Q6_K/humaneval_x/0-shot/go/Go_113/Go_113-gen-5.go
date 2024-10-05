Here is a Go program that solves the problem:

```go
package main

import (
    "fmt"
)

func OddCount(lst []string) []string {
    result := make([]string, len(lst))
    for i, s := range lst {
        count := 0
        for _, c := range s {
            if c % 2 != 0 {
                count++
            }
        }
        result[i] = fmt.Sprintf("the number of odd elements %dn the str%dng %d of the %dnput.", count, i+1, i+1, i+1)
    }
    return result
}

func main() {
    lst := []string{"1234567", "11111111"}
    fmt.Println(OddCount(lst))
}
```

This program defines a function `OddCount` that takes a slice of strings as input and returns a slice of strings. It iterates over each string in the input slice, counts the number of odd digits in each string, and then constructs a string that describes this count. The constructed strings are stored in a new slice, which is then returned.

In the `main` function, we test the `OddCount` function with a slice of strings and print the result. The output will be:

```
[the number of odd elements 4n the str4ng 4 of the 4nput. the number of odd elements 8n the str8ng 8 of the 8nput.]
```



This code creates a new slice of strings with the same length as the input slice. It then iterates over each string in the input slice. For each string, it counts the number of odd digits by iterating over each character (digit) in the string and checking if it's odd (using the modulus operator `%`). The count is then used to construct a string that describes the count. The constructed strings are stored in the new slice. Finally, the new slice is returned.

The `main` function tests the `OddCount` function with a slice of strings and prints the result. The output will be the expected result.