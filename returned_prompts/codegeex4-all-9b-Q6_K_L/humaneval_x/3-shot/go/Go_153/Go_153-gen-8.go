    var strongest_extension string
    var strongest_strength float64

    for _, extension := range extensions {
        strength := 0.0
        for _, c := range extension {
            if c >= 'A' && c <= 'Z' {
                strength++
            } else if c >= 'a' && c <= 'z' {
                strength--
            }
        }
        if strength > strongest_strength || (strength == strongest_strength && extension < strongest_extension) {
            strongest_extension = extension
            strongest_strength = strength
        }
    }

    return class_name + "." + strongest_extension
}



