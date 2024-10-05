To decode a string encoded by the `EncodeCyclic` function, you need to reverse the process. You will take the groups of three characters, and if the group has three characters, you will cycle the characters back to their original positions. 

Here is the complete code for the `DecodeCyclic` function:

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

Here's how the `DecodeCyclic` function works:

1. It splits the input string `s` into groups of three characters. If the length of the string is not a multiple of three, the last group will be shorter than three characters.

2. It creates a new group for each group in the input string. If the group has three characters, it cycles the characters back to their original positions. If the group has fewer than three characters, it leaves the group as is.

3. It joins the new groups back together into a single string.

This function should return the original string when called with a string encoded by the `EncodeCyclic` function.