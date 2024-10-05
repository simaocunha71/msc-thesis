    roman_digits := "ivxlcdm"
    roman_values := []int{1, 5, 10, 50, 100, 500, 1000}
    roman_string := ""

    for i := 0; i < len(roman_digits); i++ {
        for number >= roman_values[i] {
            number -= roman_values[i]
            roman_string += string(roman_digits[i])
        }
    }
    return strings.ToLower(roman_string)
}



