    var strongest_extension string = ""
    var strongest_strength float64 = 0
    for _, extension := range extensions {
        var strength float64 = 0
        for _, c := range extension {
            if c >= 'A' && c <= 'Z' {
                strength += float64(c - 'A' + 1)
            } else if c >= 'a' && c <= 'z' {
                strength -= float64(c - 'a' + 1)
            }
        }
        if strength > strongest_strength{
            strongest_extension = extension
            strongest_strength = strength
        }
    }
    return class_name + "." + strongest_extension
}



