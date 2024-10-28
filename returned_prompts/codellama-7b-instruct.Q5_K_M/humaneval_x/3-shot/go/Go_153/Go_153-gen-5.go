    var max_strength = 0.0
    var strongest_extension string
    for _, ext := range extensions {
        strength := float64(len(ext) - int(math.Log2(float64(len(ext)))))
        if strength > max_strength {
            max_strength = strength
            strongest_extension = ext
        }
    }
    return class_name + "." + strongest_extension
}



