    var result = make([]int, 2)
    result[0] = number + need
    if remaining-need >= 0{
        result[1] = remaining - need
    }else{
        result[1] = 0
    }
    return result
}



