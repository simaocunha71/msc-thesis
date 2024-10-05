    var strongest_extension string
    var strongest_strength float64
    for _, extension := range extensions {
        cap := 0
        sm := 0
        for _, c := range extension {
            if c >= 'A' && c <= 'Z' {
                cap++
            } else if c >= 'a' && c <= 'z' {
                sm++
            }
        }
        strength := float64(cap - sm)
        if strength > strongest_strength {
            strongest_extension = extension
            strongest_strength = strength
        }
    }
    return class_name + "." + strongest_extension
}