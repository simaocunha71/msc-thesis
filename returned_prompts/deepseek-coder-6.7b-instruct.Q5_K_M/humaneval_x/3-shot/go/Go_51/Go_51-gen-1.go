    regex, _ := regexp.Compile("[aeiouAEIOU]")
    return regex.ReplaceAllString(text, "")
}



