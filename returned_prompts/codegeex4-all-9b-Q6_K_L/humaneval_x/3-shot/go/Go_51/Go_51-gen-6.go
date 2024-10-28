    vowels := "aeiouAEIOU"

    regex := regexp.MustCompile(`[` + vowels + `]`)
    return regex.ReplaceAllString(text, "")
}



