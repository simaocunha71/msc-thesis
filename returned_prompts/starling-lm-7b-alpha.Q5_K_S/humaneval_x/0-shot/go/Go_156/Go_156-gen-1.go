    var result strings.Builder
    var mappings = []struct {
        value   int
        symbol  string
        reverse bool
    }{
        {1000, "m", false},
        {900, "cm", true},
        {500, "d", false},
        {400, "cd", true},
        {100, "c", false},
        {90, "xc", true},
        {50, "l", false},
        {40, "xl", true},
        {10, "x", false},
        {9, "ix", true},
        {5, "v", false},
        {4, "iv", true},
        {1, "i", false},
    }

    for _, mapping := range mappings {
        value := mapping.value
        symbol := mapping.symbol
        reverse := mapping.reverse

        for {
            div, mod := number/value, number%value
            if mod == 0 {
                result.WriteString(symbol)
                number -= div * value
                if number == 0 {
                    break
                }
            } else if !reverse {
                symbol += strings.Repeat(symbol, mod)
                result.WriteString(symbol)
                number -= value * (mod + 1)
                if number == 0 {
                    break
                }
            }
        }
    }

    return result.String()
}





























































































































































