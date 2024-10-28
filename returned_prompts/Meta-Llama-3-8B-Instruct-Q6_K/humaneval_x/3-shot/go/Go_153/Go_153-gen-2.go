    var strongest_extension string
    var strongest_strength float64

    for _, extension := range extensions {
        var extension_strength float64
        var upper int
        var lower int
        for _, c := range extension {
            if c >= 'A' && c <= 'Z' {
                upper++
            } else if c >= 'a' && c <= 'z' {
                lower++
            }
        }
        extension_strength = float64(upper - lower)
        if extension_strength > strongest_strength {
            strongest_extension = extension
            strongest_strength = extension_strength
        }
    }
    return class_name + "." + strongest_extension
}