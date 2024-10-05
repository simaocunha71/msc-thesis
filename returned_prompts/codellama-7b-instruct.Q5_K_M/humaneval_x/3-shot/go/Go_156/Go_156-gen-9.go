    roman_map := map[int]string{
        1: "i",
        4: "iv",
        5: "v",
        9: "ix",
        10: "x",
        40: "xl",
        50: "l",
        90: "xc",
        100: "c",
        400: "cd",
        500: "d",
        900: "cm",
        1000: "m",
    }

    result := make([]string, 0)
    for _, roman := range roman_map {
        for i := 0; i < number/len(roman); i++ {
            result = append(result, roman)
        }
        number %= len(roman)
    }
    return strings.Join(result, "")
}



