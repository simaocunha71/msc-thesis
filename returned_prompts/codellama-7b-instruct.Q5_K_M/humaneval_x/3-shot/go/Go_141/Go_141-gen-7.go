    if len(file_name) > 3{
        return "No"
    }
    if strings.Count(file_name,".") != 1{
        return "No"
    }
    if strings.Split(file_name,".")[0] == ""{
        return "No"
    }
    if !(strings.HasSuffix(file_name,".txt") || strings.HasSuffix(file_name,".exe") || strings.HasSuffix(file_name,".dll")){
        return "No"
    }
    return "Yes"
}



