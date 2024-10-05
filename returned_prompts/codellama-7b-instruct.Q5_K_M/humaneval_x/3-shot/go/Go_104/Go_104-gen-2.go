    result := make([]int, 0)
    for _, num := range x {
        if num%2 != 0{
            result = append(result, num)
        }
    }

    sort.Ints(result)
    return result
}



