    roman := []string{"i", "iv", "v", "ix", "x", "xl", "l", "xc", "c", "cd", "d", "cm", "m"}
    value := []int{1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000}
    result := ""
    i := 12
    for number > 0 {
        if number >= value[i] {
            number -= value[i]
            result += roman[i]
        } else {
            i--
        }
    }
    return strings.ToLower(result)
}



