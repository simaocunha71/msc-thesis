    sum := 0
    for _, char := range x {
        if unicode.IsUpper(char) {
            sum += int(char)
        }
    }
    return sum
}



