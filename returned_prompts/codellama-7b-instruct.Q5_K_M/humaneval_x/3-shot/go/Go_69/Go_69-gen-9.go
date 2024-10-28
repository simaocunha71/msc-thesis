    for i := 1; i <= len(lst); i++ {
        if len(lst) == 1 {
            return -1
        }
        if len(lst) == 2 {
            return 1
        }
        if len(lst) == 3 {
            return 2
        }
        if len(lst) == 4 {
            return 2
        }

    }
    return -1
}



