    regex, _ := regexp.Compile("[aeiou]")
    return regex.ReplaceAllString(text, "")
}



