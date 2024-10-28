    if len(strings.Split(file_name,".")) != 2 {
        return "No"
    }

    if len(strings.Split(file_name,".")[0]) > 3 {
        return "No"
    }

    if !strings.ContainsAny(strings.Split(file_name,".")[0],"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") {
        return "No"
    }

    if strings.Split(file_name,".")[1] != "txt" && strings.Split(file_name,".")[1] != "exe" && strings.Split(file_name,".")[1] != "dll" {
        return "No"
    }

    return "Yes"
}



