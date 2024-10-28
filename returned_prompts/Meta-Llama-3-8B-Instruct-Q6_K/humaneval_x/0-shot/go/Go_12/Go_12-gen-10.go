```go
func Longest(strings []string) interface{} {
    if len(strings) == 0 {
        return nil
    }
    maxLen := 0
    var longest string
    for _, s := range strings {
        if len(s) > maxLen {
            maxLen = len(s)
            longest = s
        }
    }
    return longest
}
```
Explanation:
This function takes a slice of strings as input and returns the longest string. If the input slice is empty, it returns nil. If there are multiple strings of the same length, it returns the first one it encounters. 

Here's how it works:

- First, it checks if the input slice is empty. If it is, it returns nil.
- It then initializes two variables: `maxLen` to store the maximum length of the strings and `longest` to store the longest string.
- It then iterates over the input slice of strings. For each string, it checks if its length is greater than `maxLen`. If it is, it updates `maxLen` and `longest` to store the new maximum length and the corresponding string.
- Finally, it returns the `longest` string.

Note that the return type of this function is `interface{}`, which means it can return values of any type, including nil. This is necessary because Go does not have a built-in way to return multiple values of different types, so we have to return a single value that can be of any type. In this case, we return either a string or nil.