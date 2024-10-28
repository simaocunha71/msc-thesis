    if x % 2 == 0 {
        if y % 2 == 0 {
            return y
        } else {
            return x
        }
    } else {
        if y % 2 == 0 {
            return -1
        } else {
            if x < y {
                return y
            } else {
                return -1
            }
        }
    }
}