```go
func Longest(strings []string) interface{} {
    if len(strings) == 0 {
        return nil
    }
    longest := strings[0]
    for _, s := range strings[1:] {
        if len(s) > len(longest) {
            longest = s
        }
    }
    return longest
}
```


Explanation:
1. Check if the input list is empty. If it is, return `nil`.
2. Initialize the `longest` variable with the first string in the list.
3. Iterate over the remaining strings in the list (starting from the second string).
4. For each string, check if its length is greater than the length of the current `longest` string.
5. If it is, update the `longest` string with the current string.
6. Once the iteration is complete, return the `longest` string.

The function returns an `interface{}` type because it may return either a string or `nil`. This is because Go does not support returning multiple types from a single function. The `interface{}` type is a generic type that can represent any value in Go, including strings and `nil`.