Here is the solution:

```go
package main

import (
    "fmt"
    "strings"
)

func TotalMatch(lst1 []string, lst2 []string) []string {
    var total1 int
    var total2 int
    for _, str := range lst1 {
        total1 += len(strings.ToLower(strings.TrimSpace(str)))
    }
    for _, str := range lst2 {
        total2 += len(strings.ToLower(strings.TrimSpace(str)))
    }
    if total1 < total2 {
        return lst1
    } else if total1 > total2 {
        return lst2
    } else {
        return lst1
    }
}

func main() {
    fmt.Println(TotalMatch([]string{}, []string{})) // []
    fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hI", "Hi"})) // ["hI", "Hi"]
    fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hi", "hi", "admin", "project"})) // ["hi", "admin"]
    fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hI", "hi", "hi"})) // ["hI", "hi", "hi"]
    fmt.Println(TotalMatch([]string{"4"}, []string{"1", "2", "3", "4", "5"})) // ["4"]
}
```

In the above code, we use a function `TotalMatch` that takes two lists of strings as parameters. We calculate the total number of characters in each list by iterating over each string in the list, trimming any leading or trailing spaces, converting the string to lowercase, and adding the length of the string to a running total. We then compare the total number of characters in each list and return the list with the smaller total. If the two lists have the same total number of characters, we return the first list. In the `main` function, we test the `TotalMatch` function with different inputs and print the results.