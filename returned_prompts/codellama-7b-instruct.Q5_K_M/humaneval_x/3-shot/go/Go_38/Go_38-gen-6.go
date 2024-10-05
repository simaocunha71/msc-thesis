    runes := []rune(s)
    groups := make([]string, 0)
    for i := 0; i < (len(s) / 3); i++ {
        groups = append(groups, string(runes[3*i : int(math.Min(float64(3*i+3), float64(len(s))))]))
    }
    newGroups := make([]string, 0)
    for _, group := range groups {
        if len(group) == 4 {
            newGroups = append(newGroups, string(append([]rune{group[0]}, group[1:]...)))
        } else {
            newGroups = append(newGroups, group)
        }
    }
    return strings.Join(newGroups, "")
}



