```go
func Longest(strings []string) interface{} {
    if len(strings) == 0 {
        return nil
    }
    maxLen := 0
    res := strings[0]
    for _, s := range strings {
        if len(s) > maxLen {
            maxLen = len(s)
            res = s
        }
    }
    return res
}
```


Explanation:

1. We check if the input slice `strings` is empty. If it is, we return `nil`.
2. We initialize `maxLen` to 0 and `res` to the first element of the slice `strings`. This is because we want to return the first string of the maximum length in case of multiple strings of the same length.
3. We iterate over the slice `strings` using a range loop. For each string `s`, we check if its length is greater than `maxLen`. If it is, we update `maxLen` and set `res` to `s`.
4. Finally, we return `res`, which is the longest string in the input slice. If the input slice is empty, `res` is `nil`. If there are multiple strings of the same maximum length, `res` is the first one encountered.