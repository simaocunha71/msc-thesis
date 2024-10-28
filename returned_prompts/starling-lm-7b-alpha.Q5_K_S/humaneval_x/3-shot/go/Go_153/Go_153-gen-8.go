    var cap_count, sm_count int
    for _, ext := range extensions {
        cap_count = 0
        sm_count = 0
        for _, c := range ext {
            if c >= 'A' && c <= 'Z' {
                cap_count++
            }else if c >= 'a' && c <= 'z' {
                sm_count++
            }
        }
        if cap_count-sm_count > 0 {
            if cap_count-sm_count == strength {
                if len(ext) < extension_len {
                    extension_name = ext
                    extension_len = len(ext)
                    strength = cap_count - sm_count
                }
            }else {
                extension_name = ext
                extension_len = len(ext)
                strength = cap_count - sm_count
            }
        }
    }
    return class_name + "." + extension_name
}



