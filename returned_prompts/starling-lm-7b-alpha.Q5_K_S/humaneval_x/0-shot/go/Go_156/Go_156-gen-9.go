    var (
        m = map[int]string{
            1000: "m",
            900:  "cm",
            500:  "d",
            400:  "cd",
            100:  "c",
            90:   "xc",
            50:   "l",
            40:   "xl",
            10:   "x",
            9:    "ix",
            5:    "v",
            4:    "iv",
            1:    "i",
        }
        r, ret []string
    )
    for k := range m {
        r = append(r, strings.Repeat(m[k], k))
    }
    for i := len(r) - 1; i >= 0; i-- {
        for number >= r[i] {
            ret = append(ret, r[i])
            number -= r[i]
        }
    }
    return strings.Join(ret, "")
}












































































































































































































































































