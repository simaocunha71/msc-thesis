    n := len(arr)
    left_pointer := 0
    right_pointer := n - 1
    result := 0
    while left_pointer < right_pointer {
        if arr[left_pointer] == arr[right_pointer] {
            left_pointer += 1
            right_pointer -= 1
        }else {
            if left_pointer == right_pointer + 1 {
                result += 1
                left_pointer += 1
                right_pointer -= 1
            }else if arr[left_pointer] == arr[left_pointer + 1] {
                result += 1
                left_pointer += 1
            }else if arr[right_pointer] == arr[right_pointer - 1] {
                result += 1
                right_pointer -= 1
            }else {
                result += 2
                left_pointer += 1
                right_pointer -= 1
            }
        }
    }
    return result
}



