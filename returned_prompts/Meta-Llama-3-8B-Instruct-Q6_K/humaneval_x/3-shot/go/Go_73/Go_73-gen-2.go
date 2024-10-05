    n := len(arr)
    left, right := 0, n-1
    changes := 0

    for left < right {
        if arr[left] != arr[right] {
            changes++
        }
        left++
        right--
    }
    return changes
}  // 1. Create two pointers, one at the start and one at the end of the array.
    // 2. Compare the elements at the two pointers.
    // 3. If they are different, increment the change counter.
    // 4. Move the pointers towards the center of the array. If the pointers are still different, increment the change counter.
    // 5. Repeat steps 2-4 until the pointers meet or cross each other. The final change counter will be the minimum number of changes needed to make the array palindromic.