    str := strconv.Itoa(x)
    if shift > len(str){
        str = ReverseString(str)
        return str
    }
    return str[shift:] + str[:shift]
}

func ReverseString(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}



