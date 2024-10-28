    if x%2 != 0 {
        if y%2 != 0 {
            return -1
        } else {
            return x
        }
    } else {
        if y%2 != 0 {
            return x
        } else {
            return y-1
        }
    }
}



