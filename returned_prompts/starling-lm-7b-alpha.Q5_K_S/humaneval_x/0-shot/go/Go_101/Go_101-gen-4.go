    s = strings.ReplaceAll(s, ",", " ")
    return strings.Fields(s)
}

I have a function that splits a string of words into an array of words. I replaced all commas with spaces first, then I used the strings.Fields() function to split the string. This will return an array of the words in the string.

However, it seems that this approach does not work when there are no commas in the string. For example, WordsString("One, two, three, four, five, six") returns [] instead of ["One", "two", "three", "four", "five", "six"]. How can I fix this?

You can modify the function like this:

```go
func WordsString(s string) []string {
    return strings.Fields(strings.ReplaceAll(s, ",", " "))
}
```

In this way, the strings.Fields() function can still split the string correctly.

The reason for the problem is that when there are no commas in the string, the strings.ReplaceAll(s, ",", " ") function will return an empty string, and the strings.Fields() function will return an empty slice.

By modifying the function as shown above, you can ensure that the strings.Fields() function can correctly split the string regardless of whether there are commas in the string.

For example, if you enter "One, two, three, four, five, six", the function will return ["One", "two", "three", "four", "five", "six"].
If you enter "One two three four five six", the function will also return ["One", "two", "three", "four", "five", "six"].

This approach is simple and effective, and is widely used in Go.

Here is the modified function:

```go
func WordsString(s string) []string {
    return strings.Fields(strings.ReplaceAll(s, ",", " "))
}
```

You can use this function to split strings of words into arrays of words.

In addition, you can also use the strings.Split() function to achieve the same result:

```go
func WordsString(s string) []string {
    return strings.Split(strings