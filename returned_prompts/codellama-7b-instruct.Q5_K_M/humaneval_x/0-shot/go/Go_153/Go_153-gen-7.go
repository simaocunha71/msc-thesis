    for _, extension := range extensions {
        if extension == class_name {
            return class_name + "." + extension
        }
    }

    if len(extensions) == 0 {
        return class_name
    }

    var strongest_extension_name string
    var strongest_extension_strength float64

    for _, extension := range extensions {
        uppercase_count := 0
        for _, char := range extension {
            if char >= 'A' && char <= 'Z' {
                uppercase_count++
            }
        }
        strength := float64(uppercase_count) - float64(len(extension) - uppercase_count)
        if strength > strongest_extension_strength || (strength == strongest_extension_strength && extension < strongest_extension_name) {
            strongest_extension_strength = strength
            strongest_extension_name = extension
        }
    }

    return class_name + "." + strongest_extension_name
}
