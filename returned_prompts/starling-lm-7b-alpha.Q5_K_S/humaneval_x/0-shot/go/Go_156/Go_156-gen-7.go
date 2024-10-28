    var result []byte
    var vals = []struct {
        num, r string
    } {
        {900, "cm" },
        {500, "d" },
        {400, "cd" },
        {100, "c" },
        {90, "xc" },
        {50, "l" },
        {40, "xl" },
        {10, "x" },
        {9, "ix" },
        {5, "v" },
        {4, "iv" },
        {1, "i" },
    }

    for i := 0; i < len(vals); i++ {
        for {
            index := strings.Index(strings.Repeat(vals[i].num, 9), fmt.Sprint(number))
            if index == 0 {
                result = append(result, []byte(vals[i].r)...)
                number -= len(vals[i].num) * index
                break
            }
        }
    }
    return string(result)
}

























































































































































































































































