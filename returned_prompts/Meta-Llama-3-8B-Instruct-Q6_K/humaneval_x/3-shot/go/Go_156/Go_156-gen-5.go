    roman_map := map[int]string{
        1000: "m",
        900: "cm",
        500: "d",
        400: "cd",
        100: "c",
        90: "xc",
        50: "l",
        40: "xl",
        10: "x",
        9: "ix",
        5: "v",
        4: "iv",
        1: "i",
    }

    roman := ""
    for k, v := range roman_map {
        for number >= k {
            roman += v
            number -= k
        }
    }
    return strings.ToLower(roman)
}