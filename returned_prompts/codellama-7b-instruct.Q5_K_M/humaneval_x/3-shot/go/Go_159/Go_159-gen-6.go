    var total_eaten = number + need
    var left = remaining - need
    if left < 0{
        left = 0
    }
    return []int{total_eaten, left}
}



