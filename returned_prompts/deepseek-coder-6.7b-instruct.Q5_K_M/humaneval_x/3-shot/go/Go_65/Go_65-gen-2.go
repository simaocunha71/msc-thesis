    str := strconv.Itoa(x)
    if shift >= len(str){
        return reverse(str)
    }

    return str[len(str)-shift:] + str[0:len(str)-shift]
}

func reverse(input string) string {
    runes := []rune(input)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}



