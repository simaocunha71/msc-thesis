To solve this problem, we can follow these steps:

1. Create a string buffer to store the result.
2. Iterate over the input string, char by char.
3. If the char is a space and the previous char is also a space, append an underscore to the buffer. If the char is a space and the previous char is not a space, append a space to the buffer. If the char is not a space, append the char to the buffer.
4. If there are more than 2 consecutive spaces, append a hyphen to the buffer.
5. Return the result string buffer.

Here's a possible implementation:

```go
func FixSpaces(text string) string {
    var buffer strings.Builder
    var lastSpace = false
    var count = 0

    for _, char := range text {
        if char == ' ' {
            if lastSpace {
                count++
                if count == 2 {
                    buffer.WriteString("-")
                    count = 0
                }
            } else {
                buffer.WriteString("_")
            }
        } else {
            buffer.WriteString(string(char))
            count = 0
        }
        lastSpace = true
    }

    return buffer.String()
}
```

This implementation has a time complexity of O(n), where n is the length of the input string.

In the above implementation, we create a string buffer to store the result. We also create two counters: `lastSpace` to check if the previous character is a space, and `count` to check if there are more than two consecutive spaces.

We iterate over the input string, char by char. If the character is a space and the previous character is also a space, we append an underscore to the buffer. If the character is a space and the previous character is not a space, we append a space to the buffer. If the character is not a space, we append the character to the buffer.

If there are more than two consecutive spaces, we append a hyphen to the buffer and reset the `count` counter.

Finally, we return the result string buffer.

This implementation has a time complexity of O(n), where n is the length of the