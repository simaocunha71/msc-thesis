    var result []int
    var min_value int = math.MaxInt32
    for i,v := range arr{
        if v % 2 == 0 && v < min_value{
            min_value = v
            result = []int{min_value, i}
        }
    }
    return result
}

