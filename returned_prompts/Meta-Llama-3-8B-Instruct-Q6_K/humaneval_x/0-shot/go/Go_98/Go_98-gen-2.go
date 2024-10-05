Here is the solution:
```go
func CountUpper(s string) int {
    count := 0
    for i := 0; i < len(s); i++ {
        if i%2 == 0 && strings.ToUpper(string(s[i])) == string(s[i]) {
            count++
        }
    }
    return count
}
```
Explanation:

* We initialize a variable `count` to 0 to keep track of the number of uppercase vowels in even indices.
* We iterate through the string `s` using a for loop.
* For each character at index `i`, we check if the index is even (using the condition `i%2 == 0`).
* If the index is even and the character is an uppercase vowel (using the condition `strings.ToUpper(string(s[i])) == string(s[i])`), we increment the `count` variable.
* Finally, we return the `count` variable.

Note that `strings.ToUpper(string(s[i])) == string(s[i])` checks if the character is an uppercase vowel by comparing it with its uppercase version. If they are the same, it means the character is an uppercase vowel. Otherwise, it's not. This condition is used to filter out lowercase vowels and other characters that are not uppercase vowels.