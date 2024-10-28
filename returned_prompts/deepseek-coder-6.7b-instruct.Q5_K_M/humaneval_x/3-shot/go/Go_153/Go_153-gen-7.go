    var strongest_extension_name string
    var strongest_extension_strength float64 = -math.MaxFloat64

    for _, extension_name := range extensions {
        var current_strength float64 = 0
        for _, c := range extension_name {
            if 'A' <= c && c <= 'Z' {
                current_strength += 1
            } else if 'a' <= c && c <= 'z' {
                current_strength -= 1
            }
        }

        if current_strength > strongest_extension_strength {
            strongest_extension_strength = current_strength
            strongest_extension_name = extension_name
        }
    }

    return class_name + "." + strongest_extension_name
}



