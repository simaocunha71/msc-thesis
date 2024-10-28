To solve this Kata, you'll need to do the following:

1. Create a function `TotalMatch` that accepts two lists of strings as parameters.
2. Initialize a variable `result` and set it to the first list.
3. Calculate the total number of characters in each list:
   - Iterate over the first list using a `for` loop, adding the length of each string to a variable `total1`.
   - Iterate over the second list using a `for` loop, adding the length of each string to a variable `total2`.
4. Compare the total number of characters in each list:
   - If `total1` is less than `total2`, set `result` to the first list.
   - If `total1` is greater than `total2`, set `result` to the second list.
   - If `total1` and `total2` are equal, set `result` to the first list.
5. Return `result`.

Here's how you can implement this solution in Go:

```go
package main

import "fmt"

func TotalMatch(lst1 []string, lst2 []string) []string {
    result := lst1

    total1 := 0
    for _, s := range lst1 {
        total1 += len(s)
    }

    total2 := 0
    for _, s := range lst2 {
        total2 += len(s)
    }

    if total1 < total2 {
        result = lst1
    } else if total1 > total2 {
        result = lst2
    }

    return result
}

func main() {
    fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hI", "Hi"})) // ["hI", "Hi"]
    fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hi", "hi", "admin", "project"})) // ["hi", "admin"]
    fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hI", "hi", "hi"})) // ["hI", "hi", "hi"]
    fmt.Println(TotalMatch([]string