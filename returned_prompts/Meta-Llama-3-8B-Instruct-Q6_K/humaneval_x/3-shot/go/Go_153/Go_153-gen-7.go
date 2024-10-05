    var strongest_extension string
    var max_strength float64
    for _, extension := range extensions {
        var strength float64
        for _, c := range extension {
            if c >= 'A' && c <= 'Z' {
                strength += 1.0
            } else {
                strength -= 1.0
            }
        }
        if strength > max_strength {
            max_strength = strength
            strongest_extension = extension
        }
    }
    return class_name + "." + strongest_extension
}