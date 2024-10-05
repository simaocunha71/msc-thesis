    if len(strings) == 0 {
        return nil
    } else {
        max := strings[0]
        for _, s := range strings {
            if len(s) > len(max) {
                max = s
            }
        }
        return max
    }
}



