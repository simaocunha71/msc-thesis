    var result string = ""
    var digits []rune = []rune(strconv.Itoa(x))

    for i := 0; i < len(digits); i++{
        if i+shift > len(digits) - 1{
            result = result + string(digits[i+shift - len(digits)])
        }else{
            result = result + string(digits[i+shift])
        }
    }
    return result
}



