    var ints  []int  
    for _, value := range values {
        if val, ok := value.(int); ok {
            ints = append(ints, val)
        }
    }
    return ints
}



