Here is the solution in Go:
```go
func CountUpper(s string) int {
    count := 0
    for i := 0; i < len(s); i += 2 {
        if strings.ToUpper(string(s[i])) == "A" || strings.ToUpper(string(s[i])) == "E" || strings.ToUpper(string(s[i])) == "I" || strings.ToUpper(string(s[i])) == "O" || strings.ToUpper(string(s[i])) == "U" {
            count++
        }
    }
    return count
}
```
Explanation:

* We iterate through the string `s` with a step size of 2, which means we only consider even indices.
* For each even index, we convert the character to uppercase using the `strings.ToUpper` function.
* We then check if the uppercase character is one of the 5 uppercase vowels ("A", "E", "I", "O", "U"). If it is, we increment the `count` variable.
* Finally, we return the `count` variable, which represents the number of uppercase vowels in even indices.