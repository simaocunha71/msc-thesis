```go
func StringSequence(n int) string {
    result := ""
    for i := 0; i <= n; i++ {
        result += strconv.Itoa(i) + " "
    }
    return result[:len(result)-1] // remove the last space
}
```


Here is how the function works:

1. Initialize an empty string `result` which will be used to store the result.
2. Iterate from 0 to `n` using a for loop.
3. Inside the loop, use `strconv.Itoa(i)` to convert the integer `i` to a string and append it to `result`. Also, append a space character to `result`.
4. After the loop, return `result`. However, we need to remove the last space character from `result` as it is not needed. To do this, use `result[:len(result)-1]` which returns a new string that is a slice of `result` up to the second last character.
5. Return the new string.