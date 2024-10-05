    var result string
    var max_strength float64 = -math.MaxFloat64
    for _, extension := range extensions {
        strength := float64(math.Ceil(float64(len(extension)) * 0.5)) - float64(math.Ceil(float64(len(extension)) * 0.3))
        if strength > max_strength {
            max_strength = strength
            result = class_name + "." + extension
        }
    }
    return result
}



