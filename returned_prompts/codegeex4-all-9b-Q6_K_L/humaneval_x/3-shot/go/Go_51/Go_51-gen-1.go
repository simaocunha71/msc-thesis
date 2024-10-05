    reg, err := regexp.Compile("[aeiouAEIOU]")
    if err != nil {
        panic(err)
    }
    return reg.ReplaceAllString(text, "")
}



