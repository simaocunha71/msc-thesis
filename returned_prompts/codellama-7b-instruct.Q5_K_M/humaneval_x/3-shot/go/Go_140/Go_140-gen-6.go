    if strings.Contains(text,"  "){
        text = strings.Replace(text,"  ","-",-1)
    }
    return strings.Replace(text," ","_",-1)
}



