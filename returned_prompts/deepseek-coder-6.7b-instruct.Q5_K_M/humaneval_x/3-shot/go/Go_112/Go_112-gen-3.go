    for _, v := range c {
        s = strings.Replace(s, string(v), "", -1)
    }
    r := []rune(s)
    for i := 0; i < len(r)/2; i++ {
        r[i], r[len(r)-1-i] = r[len(r)-1-i], r[i]
    }
    return [2]interface{}{string(r), s == string(r)}
}



