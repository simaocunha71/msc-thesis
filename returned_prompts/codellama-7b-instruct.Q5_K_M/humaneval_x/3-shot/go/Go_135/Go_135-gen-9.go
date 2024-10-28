    for i := len(arr)-2; i>=0; i--{
        if arr[i] <= arr[i+1]{
            continue
        }else{
            return i
        }
    }
    return -1
}



