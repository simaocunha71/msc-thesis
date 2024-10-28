    for _, s := range lst {
        c := 0
        for _, r := range s {
            if r%2 == 1 {
                c++
            }
        }
        fmt.Printf("the number of odd elements %d in the str%dng %d of the %dinput.\n", c, len(s), s, len(s))
    }
    return lst
}
