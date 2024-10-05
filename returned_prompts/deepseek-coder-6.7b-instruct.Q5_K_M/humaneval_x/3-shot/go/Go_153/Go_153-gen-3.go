    var strongest_extension string
    max_strength float64 = -math.MaxFloat64

    for _, extension := range extensions {
        var strength float64 = 0
        for _, char := range extension {
            if char >= 'A' && char <= 'Z' {
                strength += 1
            } else if char >= 'a' && char <= 'z' {
                strength -= 1
            }
        }
        if strength > max_strength {
            max_strength = strength
            strongest_extension = extension
        }
    }

    return class_name + "." + strongest_extension
}



