    max_strength := -math.MaxInt
    max_extension := ""

    for _, extension := range extensions {
        strength := 0
        for _, char := range extension {
            if char >= 'A' && char <= 'Z' {
                strength += 1
            } else if char >= 'a' && char <= 'z' {
                strength -= 1
            }
        }
        if strength > max_strength {
            max_strength = strength
            max_extension = extension
        }
    }

    return class_name + "." + max_extension
}