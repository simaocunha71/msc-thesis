    for _, v := range x {
        if v < 10 {
            continue A
        }
        for i := 0; i < 10; i++ {
            if v % 10 == i {
                continue A
            }
        }
        sort.Ints(x)
        return x
    }
    return x
}

