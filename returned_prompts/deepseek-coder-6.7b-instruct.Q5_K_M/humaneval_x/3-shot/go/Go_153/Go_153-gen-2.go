    var strongest_extension string
    var max_strength float64 = -math.MaxFloat64

    for _, extension := range extensions {
        cap_count := 0
        sm_count := 0
        for _, char := range extension {
            if char >= 'A' && char <= 'Z' {
                cap_count++
            } else if char >= 'a' && char <= 'z' {
                sm_count++
            }
        }
        strength := float64(cap_count) - float64(sm_count)
        if strength > max_strength {
            max_strength = strength
            strongest_extension = extension
        }
    }

    return class_name + "." + strongest_extension
}



