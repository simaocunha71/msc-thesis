    sort.Ints(arr)
    result := make([]string, 0)
    for i := 1; i < len(arr); i++ {
        if arr[i] - arr[i-1] == 1 {
            continue
        }else {
            if arr[i-1] == 1 {
                result = append(result, "One")
            }else if arr[i-1] == 2 {
                result = append(result, "Two")
            }else if arr[i-1] == 3 {
                result = append(result, "Three")
            }else if arr[i-1] == 4 {
                result = append(result, "Four")
            }else if arr[i-1] == 5 {
                result = append(result, "Five")
            }else if arr[i-1] == 6 {
                result = append(result, "Six")
            }else if arr[i-1] == 7 {
                result = append(result, "Seven")
            }else if arr[i-1] == 8 {
                result = append(result, "Eight")
            }else if arr[i-1] == 9 {
                result = append(result, "Nine")
            }

            if arr[i] - arr[i-1] == 1 {
                continue
            }else {
                if arr[i] == 1 {
                    result = append(result, "One")
                }else if arr[i] == 2 {
                    result = append(result, "Two")
                }else if arr[i] == 3 {
                    result = append(result, "Three")
                }else if arr[i] == 4 {
                    result = append(result, "Four")
                }else if arr[i] == 5 {
                    result = append(result, "Five")
                }else if arr[i] == 6 {
                    result = append(result, "Six")
                }else if arr[i] == 7 {
                    result = append(result, "Seven")
                }else