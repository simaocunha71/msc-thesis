    vals := []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}
    syms := []string{"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"}

    res := ""
    for i := 0; i < len(vals) && number > 0; i++ {
        for vals[i] <= number {
            number -= vals[i]
            res += syms[i]
        }
    }
    return strings.ToLower(res)
}



