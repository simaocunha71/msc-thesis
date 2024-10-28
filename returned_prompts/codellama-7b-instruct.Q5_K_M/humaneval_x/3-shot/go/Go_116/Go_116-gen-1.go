    // sort the array based on the number of ones in the binary representation
    // in ascending order, then sort the array based on the decimal values
    // if two numbers have the same number of ones and the same decimal value,
    // they are considered equal
    sort.Slice(arr, func(i, j int) bool {
        num_ones_i := 0
        num_ones_j := 0
        for x := 1; x < arr[i]; x *= 2 {
            if arr[i] >= x {
                num_ones_i += 1
            }
        }
        for x := 1; x < arr[j]; x *= 2 {
            if arr[j] >= x {
                num_ones_j += 1
            }
        }
        if num_ones_i != num_ones_j {
            return num_ones_i < num_ones_j
        }
        return arr[i] < arr[j]
    })
    return arr
}



