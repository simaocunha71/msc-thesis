    var result strings.Builder
    map_roman := map[int]string{
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
    for num := number; num > 0; {
        for k := range map_roman {
            if num >= k {
                result.WriteString(map_roman[k])
                num -= k
                break
            }
        }
    }
    return result.String()
}



