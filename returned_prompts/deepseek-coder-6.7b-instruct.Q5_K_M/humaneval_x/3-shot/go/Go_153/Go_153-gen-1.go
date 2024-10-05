    max_strength := math.MinInt64
    strongest_extension := ""

    for _, extension := range extensions {
        cap_letters := 0
        sm_letters := 0

        for _, char := range extension {
            if char >= 'A' && char <= 'Z' {
                cap_letters++
            } else if char >= 'a' && char <= 'z' {
                sm_letters++
            }
        }
        strength := cap_letters - sm_letters

        if strength > max_strength {
            max_strength = strength
            strongest_extension = extension
        }
    }

    return class_name + "." + strongest_extension
}

