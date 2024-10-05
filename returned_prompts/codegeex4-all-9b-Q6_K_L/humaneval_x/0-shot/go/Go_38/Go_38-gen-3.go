To decode a string that was encoded using the `EncodeCyclic` function, you need to reverse the process. Here's how you can implement the `DecodeCyclic` function:

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
            newGroups = append(newGroups, string(append(runes[2:], runes[0:2]...)))
        } else {
            newGroups = append(newGroups, group)
        }
    }
    return strings.Join(newGroups, "")
}
```

Explanation:
- The function first splits the input string into groups of up to three characters.
- It then iterates over each group.
- For groups of three characters, it reverses the order of the runes.
- For groups of less than three characters, it leaves the group as is.
- Finally, it joins all the groups back together into a single string.

This function should now correctly decode any string that was encoded using the `EncodeCyclic` function.