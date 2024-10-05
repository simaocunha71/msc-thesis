    var strongest_extension_name string = ""
    var strongest_strength float64 = 0.0

    for _, ext := range extensions {
        var strength float64 = 0.0

        for _, r := range ext {
            if r >= 'A' && r <= 'Z' {
                strength += 1
            } else {
                strength -= 1
            }
        }

        if strength > strongest_strength || (strength == strongest_strength && ext < strongest_extension_name) {
            strongest_strength = strength
            strongest_extension_name = ext
        }
    }
    return class_name + "." + strongest_extension_name
}



