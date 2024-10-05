Here is the solution in Go:
```go
func FilterByPrefix(strings []string, prefix string) []string {
    result := make([]string, 0)
    for _, s := range strings {
        if strings.HasPrefix(s, prefix) {
            result = append(result, s)
        }
    }
    return result
}
```
Explanation:

* We create an empty slice `result` to store the filtered strings.
* We iterate over the input slice `strings` using a range loop.
* For each string `s` in the input slice, we check if it starts with the given `prefix` using the `strings.HasPrefix` function.
* If the string starts with the prefix, we append it to the `result` slice using the `append` function.
* Finally, we return the `result` slice containing the filtered strings.

You can test this function with the examples you provided:
```go
package main

import "fmt"

func main() {
    strings := []string{"abc", "bcd", "cde", "array"}
    prefix := "a"
    result := FilterByPrefix(strings, prefix)
    fmt.Println(result) // Output: ["abc", "array"]
}
```