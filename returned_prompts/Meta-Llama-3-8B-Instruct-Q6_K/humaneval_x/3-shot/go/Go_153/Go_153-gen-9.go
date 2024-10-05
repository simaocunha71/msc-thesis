    var strongest_extension string
    var strongest_extension_strength float64

    for _, extension := range extensions {
        var extension_strength float64
        for _, char := range extension {
            if char >= 'A' && char <= 'Z' {
                extension_strength += 1
            } else {
                extension_strength -= 1
            }
        }
        if extension_strength > strongest_extension_strength {
            strongest_extension = extension
            strongest_extension_strength = extension_strength
        }
    }
    return class_name + "." + strongest_extension
}