    var result string

    ones := []string{"i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix"}
    tens := []string{"x", "xx", "xxx", "xl", "l", "lx", "lxx", "lxxx", "xc"}
    hundreds := []string{"c", "cc", "ccc", "cd", "d", "dc", "dcc", "dccc", "cm"}

    for number > 0 {
        if number >= 1000 {
            result += "m"
            number -= 1000
        }else if number >= 100 {
            result += hundreds[number/100-1]
            number %= 100
        }else if number >= 10 {
            result += tens[number/10-1]
            number %= 10
        }else{
            result += ones[number-1]
            break
        }
    }
    return result
}



