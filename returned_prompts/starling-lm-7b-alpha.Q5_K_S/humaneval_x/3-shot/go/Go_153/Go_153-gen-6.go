    strength_list := make(map[int64]string)
    for _, extension := range extensions {
        strength := int64(len(extension) - math.Abs(math.Cos(math.Abs(extension))))
        strength_list[strength] = extension
    }

    var max_strength int64 = -1
    for _, strength := range strength_list {
        if strength > max_strength {
            max_strength = strength
        }
    }

    return class_name + "." + strength_list[max_strength]
}



