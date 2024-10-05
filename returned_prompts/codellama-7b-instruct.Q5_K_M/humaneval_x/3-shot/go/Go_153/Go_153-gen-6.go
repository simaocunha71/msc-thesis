    if len(extensions) == 0{
        return class_name
    }

    var class_strength float64 = -1000000
    var strongest_extension string = ""
    for _, ext := range extensions{
        var ext_strength float64 = 0
        for _, c := range ext{
            if c >= 'A' && c <= 'Z'{
                ext_strength += float64(c - 'A')
            } else{
                ext_strength += float64(c - 'a' + 26)
            }
        }
        if ext_strength > class_strength{
            class_strength = ext_strength
            strongest_extension = ext
        }
    }
    return class_name + "." + strongest_extension
}



