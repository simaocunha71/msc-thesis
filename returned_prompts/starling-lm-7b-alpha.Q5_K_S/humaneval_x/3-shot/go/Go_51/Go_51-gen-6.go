    regex := regexp.MustCompile("[aeiou]")
    return regex.ReplaceAllString(text, "")
}



