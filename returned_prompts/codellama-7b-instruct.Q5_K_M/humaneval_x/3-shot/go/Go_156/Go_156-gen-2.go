    var result string
    var roman_numerals = []string{"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"}
    var values = []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}

    for i := 0; i < len(values); i++ {
        for number >= values[i] {
            result += roman_numerals[i]
            number -= values[i]
        }
    }
    return result
}



