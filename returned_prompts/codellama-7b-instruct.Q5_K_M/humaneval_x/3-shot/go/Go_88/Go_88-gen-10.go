    var sum int = 0
    for _, value := range array{
        sum += value
    }
    if sum%2 == 0{
        sort.Ints(array)
    }else{
        sort.Sort(sort.Reverse(sort.IntSlice(array)))
    }
    return array
}



