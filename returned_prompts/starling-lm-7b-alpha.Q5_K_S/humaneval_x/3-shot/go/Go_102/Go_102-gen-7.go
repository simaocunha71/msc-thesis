    if x%2 == 1 {
        x += 1
    }
    if y%2 == 0 {
        y -= 1
    }
    if y >= x {
        return y
    }
    return -1
}



