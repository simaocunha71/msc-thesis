    reg, _ := regexp.Compile("[aeiouAEIOU]")
    result := reg.ReplaceAllString(text, "")
    return result
}

