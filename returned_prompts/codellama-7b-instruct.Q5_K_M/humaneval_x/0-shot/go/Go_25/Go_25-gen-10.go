    for _, v := range math.Factorize(n) {
        if v == 1 {
            continue A
        }
        return v
    }
    return nil
}


