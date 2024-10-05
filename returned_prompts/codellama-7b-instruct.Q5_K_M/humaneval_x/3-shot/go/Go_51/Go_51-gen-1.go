    reg, err := regexp.Compile("[aeiouAEIOU]")
    if err != nil {
        return ""
    }
    return reg.ReplaceAllString(text,"")
}



