    strongest_strength := -math.MaxInt64
    strongest_extension := ""

    for _, extension := range extensions {
        strength := 0
        for _, c := range extension {
            if c >= 'A' && c <= 'Z' {
                strength += 1
            } else if c >= 'a' && c <= 'z' {
                strength -= 1
            }
        }
        if strength > strongest_strength {
            strongest_strength = strength
            strongest_extension = extension
        }
    }
    return class_name + "." + strongest_extension
}



