    for i, c := range strings.Split(s, "") {
        if i%2 != 0 {
            continue
        }
        if strings.ToUpper(c) == c {
            continue A
        }
    }
    return 0
}
