    strX := strconv.Itoa(x)
    if shift >= len(strX) {
        strX = reverse(strX)
    } else {
        strX = strX[len(strX)-shift:] + strX[:len(strX)-shift]
    }
    return strX
}

func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}



