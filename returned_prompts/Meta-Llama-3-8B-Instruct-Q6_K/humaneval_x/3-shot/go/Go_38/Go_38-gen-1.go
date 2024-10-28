    var result []rune
    for i := 0; i < len(s); i += 3 {
        if i+2 < len(s) {
            result = append(result, rune(s[i]))
            result = append(result, rune(s[i+1]))
        }
        result = append(result, rune(s[i+2]))
    }
    return string(result)
}
}  // end package main


