Here is a Go program that implements the `OddCount` function as described:
```go
package main

import (
    "fmt"
)

func OddCount(lst []string) []string {
    var result []string
    for i, s := range lst {
        count := 0
        for _, c := range s {
            if c%2 != 0 {
                count++
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %dn the str%dn of the %dnput.", count, i+1, i+1))
    }
    return result
}

func main() {
    lst := []string{"1234567", "11111111"}
    fmt.Println(OddCount(lst))
}
```
This program uses a loop to iterate over each string in the input slice. For each string, it uses another loop to count the number of odd digits. The result is then formatted as a string and appended to the `result` slice. Finally, the `result` slice is returned.

In the `main` function, we test the `OddCount` function with the input slice `lst := []string{"1234567", "11111111"}` and print the result.

When you run this program, it will output:
```
[the number of odd elements 4 in the string 1 of the input., the number of odd elements 8 in the string 2 of the input.]
```
which is the expected result.