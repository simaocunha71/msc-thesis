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
* For each string `s` in the input slice, we use the `strings.HasPrefix` function to check if it starts with the given `prefix`.
* If it does, we append it to the `result` slice using `append`.
* Finally, we return the `result` slice containing only the strings that start with the given prefix.