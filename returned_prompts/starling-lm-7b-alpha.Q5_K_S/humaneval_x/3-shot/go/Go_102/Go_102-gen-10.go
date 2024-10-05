    if x == y && x % 2 == 0 {
        return x
    }
    if x % 2 == 0 {
        return x + 1
    }
    if y % 2 == 0 {
        return y - 1
    }
    return -1
}



