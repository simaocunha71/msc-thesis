The provided `EncodeCyclic` function is designed to take a string `s` as input and return an encoded string. The encoding process involves splitting the input string into groups of three characters, and then rearranging each group by moving the first character to the end of the group. This process is repeated until all characters in the input string have been processed.

Here is the modified `DecodeCyclic` function to reverse the encoding process:

```go
func DecodeCyclic(s string) string {
    decodedGroups := make([]string, 0)
    for i := 0; i < len(s); i += 3 {
        group := s[i : i+3]
        if len(group) == 3 {
            decodedGroups = append(decodedGroups, string([]rune{group[0]} + []rune(group[1:])))
        } else {
            decodedGroups = append(decodedGroups, group)
        }
    }
    return strings.Join(decodedGroups, "")
}
```

In this `DecodeCyclic` function, we iterate over the input string `s` in steps of 3 characters. For each group of 3 characters, we check if the length of the group is 3. If it is, we rearrange the group by moving the first character to the front of the group. If the length of the group is less than 3, we assume it is the last group and append it as is to the `decodedGroups` slice. Finally, we join all the decoded groups using the `strings.Join` function to form the decoded string.