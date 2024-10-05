    sort.Ints(arr)
    result := arr[len(arr)-k:]
    sort.Ints(result)
    return result
}



