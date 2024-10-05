    var result []rune

    var x_str string =  string(intToString(x))
    var x_len = len(x_str)

    if shift > x_len {
        for _, c := range x_str {
            result = append(result, c)
        }
        return string(result)
    }

    for i := 0; i < x_len; i++ {
        j:= (i + shift) % x_len
        result = append(result, x_str[j])
    }

    return string(result)
}

func intToString(number int) []rune {
    var result []rune
    for number != 0 {
        result = append(result, rune(number%10 + '0'))
        number /= 10
    }
    return result
}



