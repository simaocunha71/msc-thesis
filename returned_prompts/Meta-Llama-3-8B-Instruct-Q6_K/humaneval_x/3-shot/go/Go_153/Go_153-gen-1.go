    strongest_extension = ""
    strongest_strength = 0

    for _, extension := range extensions {
        var cap = 0
        var sm = 0
        for i := 0; i < len(extension); i++ {
            if extension[i] >= 'A' && extension[i] <= 'Z' {
                cap++
            } else if extension[i] >= 'a' && extension[i] <= 'z' {
                sm++
            }
        }
        strength = cap - sm
        if strength > strongest_strength || (strength == strongest_strength && strongest_extension > extension) {
            strongest_extension = extension
            strongest_strength = strength
        }
    }
    return class_name + "." + strongest_extension
}