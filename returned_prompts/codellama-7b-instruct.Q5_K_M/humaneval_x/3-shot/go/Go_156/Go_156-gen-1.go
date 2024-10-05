    roman_numerals := map[int]string{
        1: "i", 4: "iv", 5: "v", 9: "ix",
        10: "x", 40: "xl", 50: "l", 90: "xcix",
        100: "c", 400: "cd", 500: "d", 900: "cm",
        1000: "m",
    }
    result := ""

    for n := 1000; n > 0; n /= 10 {
        for number >= n {
            result += roman_numerals[n]
            number -= n
        }
    }
    return strings.ToLower(result)
}



