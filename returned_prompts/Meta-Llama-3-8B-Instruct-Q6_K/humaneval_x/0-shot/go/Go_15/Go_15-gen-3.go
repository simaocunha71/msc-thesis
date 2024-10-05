```go
func StringSequence(n int) string {
    result := ""
    for i := 0; i <= n; i++ {
        result += strconv.Itoa(i) + " "
    }
    return result[:len(result)-1] // Remove the extra space at the end
}
```

Explanation:
The function `StringSequence` takes an integer `n` as input and returns a string containing space-delimited numbers starting from 0 up to `n` inclusive.

 Inside the function, an empty string `result` is initialized. A for loop is used to iterate from 0 to `n`. In each iteration, the current number `i` is converted to a string using `strconv.Itoa` and appended to the `result` string followed by a space.

 After the loop, the `result` string is returned, but with an extra step to remove the extra space at the end of the string by slicing the string from the beginning to the second last character using `[:len(result)-1]`.

 This ensures that the returned string does not have an extra space at the end. For example, if `n` is 5, the function will return the string "0 1 2 3 4 5" without the extra space at the end.