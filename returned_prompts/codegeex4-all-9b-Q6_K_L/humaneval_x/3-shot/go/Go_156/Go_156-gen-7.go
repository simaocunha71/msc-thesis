    roman := ""
    if number/1000 > 0 {
        roman += strings.Repeat("m", number/1000)
        number %= 1000
    }
    if number/100 > 0 {
        switch number / 100 {
        case 9:
            roman += "cm"
            number %= 100
        case 8:
            roman += "dccc"
            number %= 100
        case 7:
            roman += "dcc"
            number %= 100
        case 6:
            roman += "dc"
            number %= 100
        case 5:
            roman += "d"
            number %= 100
        case 4:
            roman += "cd"
            number %= 100
        case 3:
            roman += "ccc"
            number %= 100
        case 2:
            roman += "cc"
            number %= 100
        case 1:
            roman += "c"
            number %= 100
        }
    }
    if number/10 > 0 {
        switch number / 10 {
        case 9:
            roman += "xc"
            number %= 10
        case 8:
            roman += "lxxx"
            number %= 10
        case 7:
            roman += "lxx"
            number %= 10
        case 6:
            roman += "lx"
            number %= 10
        case 5:
            roman += "l"
            number %= 10
        case 4:
            roman += "xl"
            number %= 10
        case 3:
            roman += "xxx"
            number %= 10
        case 2:
            roman += "xx"
            number %= 10
        case 1:
            roman += "x"
            number %= 10
        }
    }
    if number > 0 {
        switch number {
        case 9:
            roman += "ix"
            number -= 9
        case 8:
            roman += "viii"
            number -= 8
        case 7:
            roman += "vii"
            number -= 7
        case 6:
            roman += "vi"
            number -= 6
        case 5:
            roman += "v"
            number -= 5
        case 4:
            roman += "iv"
            number -= 4
        case 3:
            roman += "iii"
