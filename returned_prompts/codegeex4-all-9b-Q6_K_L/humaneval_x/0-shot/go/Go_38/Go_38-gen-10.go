To decode a string that has been encoded using the `EncodeCyclic` function, we need to reverse the encoding process. The encoding process involves cycling the characters in groups of three. To decode, we need to cycle the characters in the opposite direction.

Here's how you can implement the `DecodeCyclic` function:

```go
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

In this function, we iterate over the groups of characters that were created during the encoding process. For each group, we take the characters in reverse order, which effectively reverses the cycling that was done during encoding. The `DecodeCyclic` function should now correctly decode any string that was encoded using the `EncodeCyclic` function.