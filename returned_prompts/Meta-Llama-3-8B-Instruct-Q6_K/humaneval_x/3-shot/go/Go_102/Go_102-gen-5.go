    if x % 2 == 0 && y % 2 == 0 {
        if x <= y {
            return y
        } else {
            return x
        }
    } else {
        return -1
    }
} 