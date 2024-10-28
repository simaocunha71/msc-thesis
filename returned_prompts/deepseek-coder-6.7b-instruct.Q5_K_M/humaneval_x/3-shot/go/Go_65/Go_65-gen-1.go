    str_x := strconv.Itoa(x)
    if shift > len(str_x) {
        return Reverse(str_x)
    }

    return str_x[len(str_x) - shift : ] + str_x[0:len(str_x) - shift]
}

func Reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes) -1; i < j; i, j = i + 1, j - 1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}



