    var strongest_extension string
    var strongest_strength float64 = -1
    for _, extension := range extensions {
        var strength float64 = -1
        for _, r := range extension {
            if r >= 'A' && r <= 'Z' {
                strength += 1
            } else if r >= 'a' && r <= 'z' {
                strength -= 1
            }
        }
        if strength > strongest_strength {
            strongest_extension = extension
            strongest_strength = strength
        }
    }
    return class_name + "." + strongest_extension
}



