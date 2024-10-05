To decode a string that was encoded with the `EncodeCyclic` function, you need to reverse the process. The process involves cycling the characters in each group of three. Here's how you can implement the `DecodeCyclic` function:

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

In the `DecodeCyclic` function, we create `newGroups` by cycling the characters in each group of three. If the group is 3 characters long, we move the second character to the end, the first character to the second position, and the third character to the first position. If the group is not 3 characters long, we simply append the group to `newGroups` as is. Finally, we join all the groups in `newGroups` into a single string and return it.