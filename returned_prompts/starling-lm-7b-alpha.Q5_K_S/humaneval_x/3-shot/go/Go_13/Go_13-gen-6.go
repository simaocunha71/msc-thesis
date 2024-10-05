    for {
        if a % b == 0 {
            return b
        } else {
            a, b = b, a % b
        }
    }
}



