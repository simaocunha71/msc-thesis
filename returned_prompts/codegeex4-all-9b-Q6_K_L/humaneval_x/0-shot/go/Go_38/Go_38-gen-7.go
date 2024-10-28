To decode a string that has been encoded using the `EncodeCyclic` function, you need to reverse the encoding process. Here's how you can implement the `DecodeCyclic` function:

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
            newGroups = append(newGroups, string(append(runes[2:], runes[0], runes[1])))
        } else {
            newGroups = append(newGroups, group)
        }
    }
    return strings.Join(newGroups, "")
}
```

In this implementation, we iterate over the groups of the encoded string. For each group of three characters, we move the first character to the end of the group. For groups that are not of length three, we leave them unchanged. Finally, we join the groups back together to form the decoded string.