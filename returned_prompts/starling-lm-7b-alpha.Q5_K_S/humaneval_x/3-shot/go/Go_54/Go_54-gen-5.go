    if len(s0) != len(s1) {
        return false
    }
    sorted0 := make([]rune, len(s0))
    sorted1 := make([]rune, len(s1))
    copy(sorted0, s0)
    copy(sorted1, s1)

    sort.Slice(sorted0, func(i, j int) bool {
        return sorted0[i] < sorted0[j]
    })
    sort.Slice(sorted1, func(i, j int) bool {
        return sorted1[i] < sorted1[j]
    })

    for i := 0; i < len(s0); i++ {
        if sorted0[i] != sorted1[i] {
            return false
        }
    }
    return true
}



