    var count int = 0
    var i int = 0
    var j int = len(arr)-1

    for {
        if arr[i] == arr[j]{
            i += 1
            j -= 1
            if i >= j{
                return count
            }
        }else{
            count += 1
            arr[i] = arr[j]
            arr[j] = arr[i]
            i += 1
            j -= 1
        }
    }
}



