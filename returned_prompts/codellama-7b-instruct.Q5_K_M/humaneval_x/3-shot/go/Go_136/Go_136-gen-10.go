    var a,b interface{}
    if len(lst) == 0{
        return [2]interface{}{a,b}
    }
    for _,v := range lst{
        if v < 0 && (a == nil || v > a.(int)){
            a = v
        }
        if v > 0 && (b == nil || v < b.(int)){
            b = v
        }
    }
    return [2]interface{}{a,b}
}



