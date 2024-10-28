    values := []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}
    numerals := []string{"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"}
    result := ""
    for i := 0; i < len(values); i++ {
        for number >= values[i] {
            number -= values[i]
            result += numerals[i]
        }
    }
    return strings.ToLower(result)
}


