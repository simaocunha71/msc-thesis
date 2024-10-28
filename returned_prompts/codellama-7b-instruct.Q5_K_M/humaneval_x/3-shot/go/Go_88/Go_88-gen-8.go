    var sum int
    for _, v := range array {
        sum += v
    }
    if sum%2 == 0 {
        sort.Sort(sort.Reverse(sort.IntSlice(array)))
    }else{
        sort.Sort(sort.IntSlice(array))
    }
    return array
}



