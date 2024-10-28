    var max_strength int = -math.MaxInt32
    var strongest_extension string
    for _, extension := range extensions {
        var strength int = 0
        for _, c := range extension {
            if c >= 'A' && c <= 'Z' {
                strength++
            } else if c >= 'a' && c <= 'z' {
                strength--
            }
        }
        if strength > max_strength {
            max_strength = strength
            strongest_extension = extension
        }
    }
    return class_name + "." + strongest_extension
}