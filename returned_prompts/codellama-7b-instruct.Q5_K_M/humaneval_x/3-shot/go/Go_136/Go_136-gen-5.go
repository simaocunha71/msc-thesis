    var a,b int
    for _, v := range lst {
        if v < 0 && v > a {
            a = v
        }else if v > 0 && v < b {
            b = v
        }
    }
    return [2]interface{}{a,b}
}



