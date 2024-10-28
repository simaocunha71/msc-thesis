    sort.Ints(arr)
    result := arr[len(arr)-k:]
    sort.Reverse(result)
    return result
}



