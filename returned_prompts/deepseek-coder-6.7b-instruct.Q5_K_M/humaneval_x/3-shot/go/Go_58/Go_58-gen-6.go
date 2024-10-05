    common_elements := []int{}

    sort.Ints(l1)
    sort.Ints(l2)

    for _, v := range l1 {
        if binarySearch(l2, v) {
            common_elements = append(common_elements, v)
        }
    }

    return common_elements
}

func binarySearch(arr []int, find int) bool {
    left, right := 0, len(arr)-1

    for left <= right {
        mid := (left + right) / 2

        if arr[mid] < find {
            left = mid + 1
        } else if arr[mid] > find {
            right = mid - 1
        } else if arr[mid] == find {
            return true
        }
    }

    return false
}



