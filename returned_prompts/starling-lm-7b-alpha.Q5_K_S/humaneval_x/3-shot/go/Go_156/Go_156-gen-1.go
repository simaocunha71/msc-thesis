    mini_roman := map[int]string{
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
    result := ""
    for number > 0 {
        for number-mini_roman[number] >= 0 {
            number -= mini_roman[number]
            result += mini_roman[number]
        }
    }
    return result
}



