Here is a solution written in Go:

```go
func Longest(strings []string) interface{} {
    if len(strings) == 0 {
        return nil
    }

    longest := strings[0]
    for _, str := range strings {
        if len(str) > len(longest) {
            longest = str
        }
    }
    return longest
}
```

This function first checks if the input list is empty, and if it is, it returns `nil`. Then it initializes a variable `longest` with the first string in the list. It then loops through the list of strings, and if it finds a string that is longer than the current `longest`, it updates `longest` to that string. Finally, it returns `longest`.

Here are some tests to verify the function:

```go
func main() {
    fmt.Println(Longest([]string{})) // nil
    fmt.Println(Longest([]string{"a", "b", "c"})) // "a"
    fmt.Println(Longest([]string{"a", "bb", "ccc"})) // "ccc"
}
```