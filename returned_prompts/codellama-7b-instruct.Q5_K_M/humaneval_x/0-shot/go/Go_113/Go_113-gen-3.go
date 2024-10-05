    for _, s := range lst {
        var cnt int
        for _, r := range s {
            if r%2 != 0 {
                cnt++
            }
        }
        fmt.Printf("the number of odd elements %d in the str%dng %d of the %dinput.", cnt, len(s), s, len(lst))
    }
    return []string{}
}
