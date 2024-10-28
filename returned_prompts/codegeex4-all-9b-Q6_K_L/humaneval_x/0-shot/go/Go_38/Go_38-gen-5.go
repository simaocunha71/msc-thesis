To decode a string that has been encoded with the `EncodeCyclic` function, you need to reverse the process. Here's how you can do it:

1. Split the encoded string into groups of three characters.
2. For each group, reverse the order of the characters.
3. Concatenate the groups back together to form the decoded string.

Here's the implementation of the `DecodeCyclic` function:

```go
// takes as input string encoded with EncodeCyclic function. Returns decoded string.
func DecodeCyclic(s string) string {
    groups := make([]string, 0)
    for i := 0; i < ((len(s) + 2) / 3); i++ {
        groups = append(groups, s[3*i:int(math.Min(float64(3*i+3), float64(len(s))))])
    }
    newGroups := make([]string, 0)
    for _, group := range groups {
        runes := []rune(group)
        if len(group) == 3 {
            newGroups = append(newGroups, string(append(runes[2:], runes[0:2]...)))
        } else {
            newGroups = append(newGroups, group)
        }
    }
    return strings.Join(newGroups, "")
}
```

In this implementation, we use slicing and concatenation to reverse the order of the characters in each group. If the group has three characters, we move the first character to the end, and the other two characters move up one position. If the group has fewer than three characters, we leave it as is. Finally, we join the groups back together with no separator, resulting in the original string before encoding.