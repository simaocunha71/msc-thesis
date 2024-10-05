    if number < 1 || number > 1000 {
        return ""
    }

    roman_numerals := []string{"i", "x", "c", "m"}
    roman_values := []int{1, 10, 100, 1000}
    result := ""

    for i := len(roman_values) - 1; i >= 0; i-- {
        value := roman_values[i]
        count := number / value
        if count > 0 {
            result += strings.Repeat(roman_numerals[i], count)
            number %= value
        }
    }

    return result
}

