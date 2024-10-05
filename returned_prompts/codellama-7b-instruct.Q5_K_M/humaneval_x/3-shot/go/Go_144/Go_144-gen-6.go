    var a, b int
    var c, d int
    _, err := fmt.Sscanf(x, "%d/%d", &a, &b)
    if err != nil {
        return false
    }
    _, err = fmt.Sscanf(n, "%d/%d", &c, &d)
    if err != nil {
        return false
    }
    var f1, f2 = a*d, b*c
    var r1, r2 = f1%f2, f2%f1
    return r1 == 0 && r2 == 0
}



