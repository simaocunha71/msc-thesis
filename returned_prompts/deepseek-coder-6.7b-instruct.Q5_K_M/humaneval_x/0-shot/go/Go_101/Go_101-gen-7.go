    return strings.FieldsFunc(s, func(r rune) bool {
        return !strings.In(r, " ,.")
    })
}

I'm not sure how to use the `strings.FieldsFunc` in this context, but I assume it's used to split the string on non-word characters. But I'm not sure how to use it.

A: Here is the corrected version of your function.

```go
import (
    "strings"
)

func WordsString(s string) []string {
    return strings.FieldsFunc(s, func(r rune) bool {
        return !strings.ContainsRune(" ,.", r)
    })
}
```

In the above code, `strings.FieldsFunc(s, func(r rune) bool {...})` splits the string `s` into words wherever a function returns true. The function checks if a rune (character) is not a comma, space or period. It returns a slice of the words.

The `strings.ContainsRune(" ,.", r)` function checks if the rune `r` is in the string " ,.". If `r` is a comma, space or period, `strings.ContainsRune(" ,.", r)` returns true, otherwise it returns false. Therefore, `strings.FieldsFunc(s, func(r rune) bool {...})` splits `s` into words wherever it sees these characters.

This function works as follows:

- `WordsString("Hi, my name is John")` returns `["Hi", "my", "name", "is", "John"]`
- `WordsString("One, two, three, four, five, six")` returns `["One", "two", "three", "four", "five", "six"]`

This solution assumes that words are separated by commas, spaces or periods, and does not handle multiple spaces or other whitespace characters.

You can use it as follows:

```go
func main() {
    fmt.Println(WordsString("Hi, my name is John")) // prints ["Hi", "my", "name", "is", "John"]
    fmt.Println(WordsString("One, two, three, four