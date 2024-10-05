    for _, v := range lst {
        if v < 0 || v != math.Floor(v) {
            continue A
        }
    }
    return 0
}
