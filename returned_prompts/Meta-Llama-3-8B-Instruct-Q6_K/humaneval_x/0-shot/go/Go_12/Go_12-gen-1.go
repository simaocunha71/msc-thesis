```go
func Longest(strings []string) interface{} {
    if len(strings) == 0 {
        return nil
    }
    var longest string
    for _, s := range strings {
        if len(s) > len(longest) {
            longest = s
        }
    }
    return longest
}
```


Explanation:
The function takes a list of strings as input and returns the longest one. If the input list is empty, it returns nil. If there are multiple strings of the same length, it returns the first one it encounters.

We first check if the input list is empty. If it is, we return nil.

Then, we initialize a variable `longest` to an empty string. We iterate over the input list using a for loop. For each string `s` in the list, we check if its length is greater than the length of `longest`. If it is, we update `longest` to be `s`.

Finally, we return `longest`, which is the longest string in the input list. If the input list is empty, `longest` remains an empty string, so we return nil in that case. If there are multiple strings of the same length, `longest` is updated to the first one it encounters, so we return that one.