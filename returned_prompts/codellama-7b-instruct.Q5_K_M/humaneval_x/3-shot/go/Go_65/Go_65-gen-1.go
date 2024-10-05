    if shift > 0 {
        return string([]rune(string(x)[:shift]) + string([]rune(string(x)[shift:])) + string([]rune(string(x)[:shift])))
    } else if shift < 0 {
        return string([]rune(string(x)[shift:]) + string([]rune(string(x)[:shift])) + string([]rune(string(x)[shift:])))
    } else {
        return string([]rune(string(x)))
    }
}



