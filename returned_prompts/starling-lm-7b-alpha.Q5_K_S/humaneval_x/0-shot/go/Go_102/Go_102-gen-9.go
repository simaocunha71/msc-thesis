
if x%2 == 1 && y%2 == 1 {
    return -1
}

if x%2 == 0 {
    return x
}

if y%2 == 0 {
    return y
}

if x%2 == 1 && y%2 == 0 {
    return y
}

if x%2 == 0 && y%2 == 1 {
    return x
}

return -1
}

// Another variant:
func ChooseNum(x, y int) int {
    if x%2 == 1 && y%2 == 1 {
        return -1
    }
    if (x/2)%2 == 0 {
        return x
    }
    if (y/2)%2 == 0 {
        return y
    }
    return -1
}

// Yet another variant:
func ChooseNum(x, y int) int {
    if x%2 == 1 && y%2 == 1 {
        return -1
    }
    if x%2 == 0 {
        return x
    }
    return y
}

// Yet another variant:
func ChooseNum(x, y int) int {
    if x%2 == 1 && y%2 == 1 {
        return -1
    }
    return (x + y) / 2
}



























































































































































































