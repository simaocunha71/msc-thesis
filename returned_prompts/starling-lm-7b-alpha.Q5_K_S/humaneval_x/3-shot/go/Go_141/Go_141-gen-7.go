    var result string

    if len(file_name) > 3 {
        result = "No"
    }else if strings.Count(file_name,".") != 1 {
        result = "No"
    }else if len(file_name[:strings.Index(file_name,".")]) > 1 {
        result = "No"
    }else if len(file_name[strings.Index(file_name,"."):]) != 3 {
        result = "No"
    }else if file_name[:1] < "A" || file_name[:1] > "Z" {
        result = "No"
    }else if file_name[:1] < "a" || file_name[:1] > "z" {
        result = "No"
    }else if file_name[len(file_name)-3:] != "txt" && file_name[len(file_name)-3:] != "dll" && file_name[len(file_name)-3:] != "exe" {
        result = "No"
    }else {
        result = "Yes"
    }

    return result
}



