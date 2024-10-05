    result := append([]int(nil), array...)
    sort.Ints(result)
    if (result[0]+result[len(result)-1])%2 == 1 {
        return result
    }
    for i, j := 0, len(result)-1; i < j; i, j = i+1, j-1 {
        result[i], result[j] = result[j], result[i]
    }
    return result
}



