    var result strings.Builder
    for _, word := range strings.Split(s," ") {
        result.WriteString(ReverseString(word)+" ")
    }
    return result.String()
}



