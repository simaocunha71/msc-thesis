    var result string
    for _, r := range s {
        if len(result) % 3 == 0 {
            result += string(r)
        } else {
            result = string([]rune{result[len(result)-1]} + []rune{r})
        }
    }
    return result
}
// takes as input string and returns encoded string by cycling groups of three characters.
func EncodeCyclic(s string) string {
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

// takes as input string encoded with EncodeCyclic function. Returns decoded string.
func DecodeCyclic(s string) string {
    var result string
    for _, r := range s {
        if len(result) % 3 == 0 {
            result += string(r)
        } else {
            result = string([]rune{result[len(result)-1]} + []rune{r})
        }
    }
    return result
}