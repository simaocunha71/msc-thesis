    roman_numeral := make([]string, 0)
    roman_map := map[int]string{
        1: "i",
        5: "v",
        10: "x",
        50: "l",
        100: "c",
        500: "d",
        1000: "m",
    }

    for i, roman := range roman_map {
        for j := 0; j < number / i; j++ {
            roman_numeral = append(roman_numeral, roman)
        }
        number %= i
    }
    return strings.Join(roman_numeral, "")
}



