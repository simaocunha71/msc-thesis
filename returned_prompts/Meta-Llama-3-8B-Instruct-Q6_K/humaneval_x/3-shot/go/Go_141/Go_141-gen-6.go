    if !strings.Contains(file_name,"."){
        return "No"
    }
    parts := strings.Split(file_name,".")
    if len(parts) != 2{
        return "No"
    }
    if !strings.HasPrefix(parts[0], "a-zA-Z"){
        return "No"
    }
    if len(strings.Replace(parts[0], ".", "", -1)) > 3 {
        return "No"
    }
    if !strings.HasSuffix(parts[1], "txt") && !strings.HasSuffix(parts[1], "exe") && !strings.HasSuffix(parts[1], "dll"){
        return "No"
    }
    return "Yes"
}