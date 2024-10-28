    for _,v := range c {
        s = strings.Replace(s, string(v), "", -1)
    }
    r := [2]interface{}{s, s == Reverse(s)}
    return r
}

func Reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}


