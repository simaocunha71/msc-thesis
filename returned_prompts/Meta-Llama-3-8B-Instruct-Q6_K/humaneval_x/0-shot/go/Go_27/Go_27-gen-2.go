Here is the solution:
```go
func FlipCase(str string) string {
    var result strings.Builder
    for _, c := range str {
        if strings.ToLower(string(c)) == string(c) {
            result.WriteString(strings.ToUpper(string(c)))
        } else {
            result.WriteString(strings.ToLower(string(c)))
        }
    }
    return result.String()
}
```
Here's an explanation of the code:

* We use a `strings.Builder` to build the resulting string.
* We iterate over each character `c` in the input string `str`.
* For each character, we check if it's lowercase by converting it to lowercase using `strings.ToLower` and comparing it to the original character using `==`. If it's lowercase, we convert it to uppercase using `strings.ToUpper`.
* If it's not lowercase (i.e., it's uppercase), we convert it to lowercase using `strings.ToLower`.
* We append the resulting character to the `result` string builder using `WriteString`.
* Finally, we return the resulting string using `String` on the `result` builder.