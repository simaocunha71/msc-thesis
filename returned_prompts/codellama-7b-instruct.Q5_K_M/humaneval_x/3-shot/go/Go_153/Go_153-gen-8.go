    var class_name_length int = len(class_name)
    var strongest_extension string = ""
    var strongest_extension_strength float64 = 0
    var current_extension string = ""
    var current_extension_strength float64 = 0

    for _, extension := range(extensions){
        var extension_length int = len(extension)
        if class_name_length >= extension_length {
            continue
        }
        for _, letter := range(extension){
            if string(letter) == string(class_name[0]){
                current_extension_strength += 1
            }else if string(letter) == string(class_name[0]-32){
                current_extension_strength += 0.5
            }
        }
        if current_extension_strength > strongest_extension_strength{
            strongest_extension_strength = current_extension_strength
            strongest_extension = extension
        }
    }
    return class_name + "." + strongest_extension
}



