    if number < 1 || number > 1000 {
        panic("Invalid number")
    }

    result := make([]rune, 0)
    roman_values := []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}
    roman_symbols := []rune{'m', 'cm', 'd', 'cd', 'c', 'xc', 'l', 'xl', 'x', 'ix', 'v', 'iv', 'i'}

    for i := 0; i < len(roman_values); i++ {
        for number >= roman_values[i] {
            result = append(result, roman_symbols[i])
            number -= roman_values[i]
        }
    }

    return string(result)
}



