    var min_changes int = 0
    var max_value int = 0
    var min_value int = 0

    for _, value := range arr{
        if value > max_value{
            max_value = value
        }
        if value < min_value{
            min_value = value
        }
    }

    for _, value := range arr{
        if value - min_value > max_value - value{
            min_changes += max_value - value
        }else{
            min_changes += value - min_value
        }
    }
    return min_changes
}



