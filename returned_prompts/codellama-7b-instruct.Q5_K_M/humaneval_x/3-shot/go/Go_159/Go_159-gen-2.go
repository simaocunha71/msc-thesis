    result := make([]int, 2)
    result[0] = number + remaining
    result[1] = 0

    if (result[0] >= need){
        result[0] -= need
        result[1] = need
    }
    return result
}



