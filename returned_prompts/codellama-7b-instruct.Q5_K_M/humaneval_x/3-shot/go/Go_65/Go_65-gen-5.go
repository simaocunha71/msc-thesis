    var result []rune = []rune(string(x))
    var length int = len(result)
    if length == 1{
        return string(result[0])
    }

    for i := 0; i < shift; i++ {
        var last_char rune = result[length - 1]
        for j := length - 1; j > 0; j-- {
            result[j] = result[j - 1]
        }
        result[0] = last_char
    }
    return string(result)
}



