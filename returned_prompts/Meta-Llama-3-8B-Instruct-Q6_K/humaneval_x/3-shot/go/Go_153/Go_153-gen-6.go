    max_strength := -10000
    strongest_extension := ""

    for _, extension := range extensions {
        var strength int
        for _, c := range extension {
            if c >= 'A' && c <= 'Z' {
                strength++
            } else {
                strength--
            }
        }
        if strength > max_strength {
            max_strength = strength
            strongest_extension = extension
        }
    }
    return class_name + "." + strongest_extension
}