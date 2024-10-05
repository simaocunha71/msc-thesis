    class_name_len := len(class_name)
    class_strength := 0
    for _, e := range extensions {
        e_len := len(e)
        e_strength := e_len - class_name_len
        if e_strength > class_strength {
            class_name = class_name + "." + e
            class_strength = e_strength
        } else if e_strength == class_strength {
            if e < class_name {
                class_name = class_name + "." + e
                class_strength = e_strength
            }
        }
    }
    return class_name
}



