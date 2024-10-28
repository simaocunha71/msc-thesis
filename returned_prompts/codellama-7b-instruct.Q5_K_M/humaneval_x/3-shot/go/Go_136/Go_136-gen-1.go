    var smallest, largest *int
    for _, v := range lst{
        if v >= 0{
            if smallest == nil{
                smallest = &v
            } else if v < *smallest{
                smallest = &v
            }
        }else{
            if largest == nil{
                largest = &v
            } else if v > *largest{
                largest = &v
            }
        }
    }
    return [2]interface{}{*largest, *smallest}
}



