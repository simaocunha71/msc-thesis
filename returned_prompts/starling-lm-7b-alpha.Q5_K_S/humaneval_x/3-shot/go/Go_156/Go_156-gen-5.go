    if number < 1 || number > 1000 {
        panic("number must be between 1 and 1000")
    }
    var result strings.Builder

    map_values := map[int]string{
        1000: "m",
        900:  "cm",
        500:  "d",
        400:  "cd",
        100:  "c",
        90:   "xc",
        50:   "l",
        40:   "xl",
        10:   "x",
        9:    "ix",
        5:    "v",
        4:    "iv",
        1:    "i",
    }
    for number, roman := range map_values {
        for number {
            result.WriteString(roman)
            number -= number
        }
    }
    return result.String()
}



