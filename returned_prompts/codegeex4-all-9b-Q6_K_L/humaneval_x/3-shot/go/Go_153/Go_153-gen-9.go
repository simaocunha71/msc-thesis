    max_strength := -math.MaxFloat64
    best_extension := ""

    for _, extension := range extensions {
        strength := 0

        for _, c := range extension {
            if c >= 'A' && c <= 'Z' {
                strength += 1
            } else if c >= 'a' && c <= 'z' {
                strength -= 1
            }
        }

        if strength > max_strength {
            max_strength = strength
            best_extension = extension
        }
    }

    return class_name + "." + best_extension
}



