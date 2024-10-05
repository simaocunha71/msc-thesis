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

// Given a string, it returns the string with all its characters reversed.
func ReverseString(s string) string {
    runes := []rune(s)
    for i := 0; i < len(runes)/2; i++ {
        runes[i], runes[len(runes)-1-i] = runes[len(runes)-1-i], runes[i]
    }
    return string(runes)
}



