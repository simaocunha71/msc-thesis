    var result int = 0
    for i:=0;i<k;i++{
        var num_str string = strconv.Itoa(arr[i])
        if len(num_str)<=2{
            result += arr[i]
        }
    }
    return result
}



