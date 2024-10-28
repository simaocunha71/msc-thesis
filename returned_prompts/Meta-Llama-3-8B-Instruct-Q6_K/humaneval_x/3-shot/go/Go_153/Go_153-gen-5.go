    var strongest_extension string
    var max_strength float64

    for _, extension := range extensions {
        var strength float64
        var cap int
        var sm int
        for _, c := range extension {
            if c >= 'A' && c <= 'Z' {
                cap++
            } else if c >= 'a' && c <= 'z' {
                sm++
            }
        }
        strength = float64(cap - sm) / float64(len(extension))
        if strength > max_strength {
            max_strength = strength
            strongest_extension = extension
        }
    }
    return class_name + "." + strongest_extension
}