You can solve this problem by iterating over the string and checking if the character at each even index is an uppercase vowel. If it is, increment a counter. Here is a possible solution in Go:
```go
func CountUpper(s string) int {
    var count int
    for i, c := range s {
        if i%2 == 0 && strings.Contains("AEIOU", strings.ToUpper(string(c))) {
            count++
        }
    }
    return count
}
```
Here's an explanation of the code:

1. We initialize a variable `count` to 0, which will store the count of uppercase vowels in even indices.
2. We iterate over the string `s` using a range loop, which gives us the index `i` and the character `c` at each iteration.
