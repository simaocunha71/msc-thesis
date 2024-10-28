```go
func StringSequence(n int) string {
    var result string
    for i := 0; i <= n; i++ {
        result += strconv.Itoa(i) + " "
    }
    return result[:len(result)-1] // remove the extra space at the end
}
```

Explanation:
The function `StringSequence` takes an integer `n` as input and returns a string containing space-delimited numbers from 0 to `n` inclusive.

The function uses a for loop to iterate from 0 to `n`. Inside the loop, it converts each integer `i` to a string using `strconv.Itoa(i)` and appends it to the `result` string along with a space character using the `+=` operator.

After the loop, it removes the extra space at the end of the `result` string by using `result[:len(result)-1]`. This is because the last iteration of the loop appends a space character, which is not needed.

Finally, the function returns the `result` string.