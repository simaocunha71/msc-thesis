To solve this problem, we will iterate through the string and check each character at even indices. If the character is an uppercase vowel (A, E, I, O, U), we will increment a counter. Finally, we will return the counter as the result.

Here's the solution in Go:

```go
func CountUpper(s string) int {
    counter := 0
    for i, char := range s {
        if i%2 == 0 && (char == 'A' || char == 'E' || char == 'I' || char == 'O' || char == 'U') {
            counter++
        }
    }
    return counter
}
```

Let's test the function with the provided examples:

```go
func main() {
    fmt.Println(CountUpper("aBCdEf"))    // 1
    fmt.Println(CountUpper("abcdefg"))   // 0
    fmt.Println(CountUpper("dBBE"))      // 0
}
```

The function should return the expected results.