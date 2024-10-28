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
            newGroups = append(newGroups, string(append(runes[1:], runes[0])))
        } else {
            newGroups = append(newGroups, group)
        }
    }
    return strings.Join(newGroups, "")
}
```

In the DecodeCyclic function, we first split the input string into groups of three characters. Then, for each group, we rotate the characters back to their original positions by swapping the first and the second characters. Finally, we join the groups back into a single string and return the result.