    if len(arr)==0{
        return true
    }
    // sort.Ints(arr)
    sort.Slice(arr, func(i, j int) bool {
        return arr[i] < arr[j]
    })

    var last_element int = arr[0]
    var decreasing_count int = 0

    for _, element := range arr[1:]{
        if element < last_element{
            decreasing_count += 1
            last_element = element
        }
    }

    if decreasing_count==0{
        return true
    }

    return false
}



