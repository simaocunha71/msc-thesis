    max_strength := 0
    result := ""

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
            result = class_name + "." + extension
        }
    }
    return result
}



