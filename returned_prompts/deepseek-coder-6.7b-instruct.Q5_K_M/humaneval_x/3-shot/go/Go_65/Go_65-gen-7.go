    strX := strconv.Itoa(x)
    if shift > len(strX){
        return reverse(strX)
    }
    return strX[len(strX)-shift:] + strX[:len(strX)-shift]
}

func reverse(input string) string {
    runes := []rune(input)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}



