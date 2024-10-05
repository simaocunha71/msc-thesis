    sort.Ints(arr)
    result := make([]int,0,k)
    for i := 0;i < k;i++{
        result = append(result,arr[len(arr)-i-1])
    }
    return result
}



