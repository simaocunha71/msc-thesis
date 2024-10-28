    var max_strength int = 0
    var strongest_extension string

    for _, ext := range extensions {
        var strength int = 0
        for _, c := range ext {
            if c >= 'A' && c <= 'Z' {
                strength += int(c - 'A' + 1)
            }
        }
        if strength > max_strength {
            max_strength = strength
            strongest_extension = ext
        }
    }
    return class_name + "." + strongest_extension
}



