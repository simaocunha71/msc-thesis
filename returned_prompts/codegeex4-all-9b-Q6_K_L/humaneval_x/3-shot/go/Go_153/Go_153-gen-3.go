    max_strength := -math.MaxFloat64
    max_strength_index := 0
    for i, extension := range extensions {
        strength := 0
        for _, c := range extension {
            if c >= 'A' && c <= 'Z' {
                strength++
            } else if c >= 'a' && c <= 'z' {
                strength--
            }
        }
        if strength > max_strength {
            max_strength = strength
            max_strength_index = i
        }
    }
    return class_name + "." + extensions[max_strength_index]
}

