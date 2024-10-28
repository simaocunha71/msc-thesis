Here is a simple implementation using the `strings.Split` function:
```go
func WordsString(s string) []string {
    return strings.Split(s, " ")
}
```
This function splits the input string `s` into words using the space character (`" "`) as the separator, and returns the resulting slice of strings.

For example:
```go
fmt.Println(WordsString("Hi, my name is John")) // Output: ["Hi,", "my", "name", "is", "John"]
fmt.Println(WordsString("One, two, three, four, five, six")) // Output: ["One,", "two,", "three,", "four,", "five,", "six"]
```
Note that the resulting slice of strings includes the commas as part of the words. If you want to remove the commas, you can use the `strings.ReplaceAll` function