    var number_of_dots, number_of_digits int
    var file_extension string
    for _, c := range file_name {
        if c == '.' {
            number_of_dots += 1
            file_extension = strings.ToLower(file_name[number_of_dots:])
        }else if (c >= '0' && c <= '9') {
            number_of_digits += 1
        }
    }

    if number_of_dots == 1 && number_of_digits <= 3 {
        var allowed_extensions []string = []string{"txt", "exe", "dll"}
        for _, extension := range allowed_extensions {
            if extension == file_extension {
                return "Yes"
            }
        }
    }

    return "No"
}



