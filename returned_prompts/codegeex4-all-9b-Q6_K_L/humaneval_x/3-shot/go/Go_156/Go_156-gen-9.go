    roman := ""
    if number >= 1000 {
        roman += strings.Repeat("m", number/1000)
        number = number % 1000
    }
    if number >= 900 {
        roman += "cm"
        number = number % 900
    }
    if number >= 500 {
        roman += "d"
        number = number % 500
    }
    if number >= 400 {
        roman += "cd"
        number = number % 400
    }
    if number >= 100 {
        roman += strings.Repeat("c", number/100)
        number = number % 100
    }
    if number >= 90 {
        roman += "xc"
        number = number % 90
    }
    if number >= 50 {
        roman += "l"
        number = number % 50
    }
    if number >= 40 {
        roman += "xl"
        number = number % 40
    }
    if number >= 10 {
        roman += strings.Repeat("x", number/10)
        number = number % 10
    }
    if number >= 9 {
        roman += "ix"
        number = number % 9
    }
    if number >= 5 {
        roman += "v"
        number = number % 5
    }
    if number >= 4 {
        roman += "iv"
        number = number % 4
    }
    if number >= 1 {
        roman += strings.Repeat("i", number)
    }
    return roman
}



