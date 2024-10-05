    if sum(array[0],array[len(array)-1])%2 == 0 {
        array = sort.IntSlice(array).Desc()
    }else {
        array = sort.IntSlice(array).Asc()
    }
    return array
}



