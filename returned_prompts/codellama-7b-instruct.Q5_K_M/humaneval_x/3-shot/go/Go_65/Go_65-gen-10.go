    var result int = x % 10
    for i := 0; i < shift; i++ {
        result = (result * 10) + (x / 10)
        x = x % 10
    }
    return string(rune(result)) + string(rune(x))
}



