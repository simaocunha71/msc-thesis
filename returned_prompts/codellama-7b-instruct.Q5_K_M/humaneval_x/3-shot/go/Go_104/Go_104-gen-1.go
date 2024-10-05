    var result []int
    for _, v := range x {
        if strconv.Itoa(v)[1:len(strconv.Itoa(v))-1] == "0" {
            continue
        }else{
            result = append(result, v)
        }
    }
    sort.Ints(result)
    return result
}



