    class_name = class_name + "."

    if len(extensions) == 0 {
        return class_name
    }

    strongest_extension := extensions[0]
    strongest_strength := math.Mod(float64(len(strongest_extension)) - len(strongest_extension), 1)

    for _, extension := range extensions[1:] {
        strength := math.Mod(float64(len(extension)) - len(extension), 1)
        if strength > strongest_strength {
            strongest_extension = extension
            strongest_strength = strength
        }else if strength == strongest_strength {
            if extension < strongest_extension {
                strongest_extension = extension
            }
        }
    }

    return class_name + strongest_extension
}



