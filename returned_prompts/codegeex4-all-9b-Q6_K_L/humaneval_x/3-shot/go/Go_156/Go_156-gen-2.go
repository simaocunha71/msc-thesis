    roman := make([]string, 0)
    if number >= 1000 {
        roman = append(roman, "m")
        number -= 1000
    }
    if number >= 900 {
        roman = append(roman, "cm")
        number -= 900
    }
    if number >= 500 {
        roman = append(roman, "d")
        number -= 500
    }
    if number >= 400 {
        roman = append(roman, "cd")
        number -= 400
    }
    if number >= 100 {
        roman = append(roman, "c")
        number -= 100
    }
    if number >= 90 {
        roman = append(roman, "xc")
        number -= 90
    }
    if number >= 50 {
        roman = append(roman, "l")
        number -= 50
    }
    if number >= 40 {
        roman = append(roman, "xl")
        number -= 40
    }
    if number >= 10 {
        roman = append(roman, "x")
        number -= 10
    }
    if number >= 9 {
        roman = append(roman, "ix")
        number -= 9
    }
    if number >= 5 {
        roman = append(roman, "v")
        number -= 5
    }
    if number >= 4 {
        roman = append(roman, "iv")
        number -= 4
    }
    if number >= 1 {
        roman = append(roman, "i")
        number -= 1
    }
    return strings.Join(roman, "")
}

