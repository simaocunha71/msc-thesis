    vowels := []rune{'a', 'e', 'i', 'o', 'u', 'y'}
    regex := regexp.MustCompile(`[aeiouy]`)
    return regex.ReplaceAllString(text, "")
}



