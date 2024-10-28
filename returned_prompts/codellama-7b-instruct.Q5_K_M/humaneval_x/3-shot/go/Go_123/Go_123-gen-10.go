    result := make([]int, 0)
    current := n

    for current != 1{
        if current%2 == 0{
            current = current/2
        }else{
            current = 3*current + 1
        }
        result = append(result, current)
    }
    sort.Ints(result)
    return result
}



