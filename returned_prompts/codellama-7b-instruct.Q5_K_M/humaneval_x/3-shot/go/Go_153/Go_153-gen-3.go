    var strongest_extension string
    var strongest_strength float64 = -1

    for _, extension := range extensions {
        var strength float64 = float64(len(extension)) - float64(strings.ToLower(extension))
        if strength > strongest_strength {
            strongest_strength = strength
            strongest_extension = extension
        }
    }
    return class_name + "." + strongest_extension
}



