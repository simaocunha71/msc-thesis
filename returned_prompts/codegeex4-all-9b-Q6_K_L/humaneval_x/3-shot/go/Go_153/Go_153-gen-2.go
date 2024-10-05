    var max_strength float64 = -math.MaxFloat64
    var max_extension string = ""
    for _, extension := range extensions {
        var strength float64 = 0
        for _, c := range extension {
            if c >= 'A' && c <= 'Z' {
                strength += 1
            } else if c >= 'a' && c <= 'z' {
                strength -= 1
            }
        }
        if strength > max_strength {
            max_strength = strength
            max_extension = extension
        }
    }
    return class_name + "." + max_extension
}



