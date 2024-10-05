    sum := 0
    for _, v := range array{
        sum += v
    }

    if sum%2 != 0{
        sort.Ints(array)
    }else{
        sort.Sort(sort.Reverse(sort.IntSlice(array)))
    }

    return array
}



