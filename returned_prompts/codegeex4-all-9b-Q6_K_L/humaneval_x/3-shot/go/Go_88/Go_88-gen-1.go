    if len(array) == 0 {
        return array
    }

    var sum int = array[0] + array[len(array)-1]

    if (sum % 2) == 0 {
        sort.Slice(array, func(i, j int) bool {
            return array[i] > array[j]
        })
    } else {
        sort.Ints(array)
    }

    return array
}



