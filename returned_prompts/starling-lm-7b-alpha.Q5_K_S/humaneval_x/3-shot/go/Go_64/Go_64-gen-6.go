    result := 0
    for _, char := range s {
        if char == 'a' || char == 'e' || char == 'i' || char == 'o' || char == 'u' || (char == 'y' && strings.HasSuffix(s, "y")) {
            result += 1
        }
    }
    return result
}



