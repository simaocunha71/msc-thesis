    vowels := regexp.MustCompile(`[AEIOUaeiou]`)
    return vowels.ReplaceAllString(text, "")
}



