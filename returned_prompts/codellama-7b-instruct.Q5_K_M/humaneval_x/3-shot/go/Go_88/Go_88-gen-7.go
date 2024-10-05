    var sum int = array[0] + array[len(array)-1]
    var result []int

    if sum%2 == 0{
        result = array
        sort.Sort(sort.Reverse(sort.IntSlice(result)))
    }else{
        result = array
        sort.Ints(result)
    }
    return result
}



