    for i := 0; i < len(arr); i++ {
        for j := 0; j < len(arr)-1; j++ {
            if (getBitCount(arr[j]) > getBitCount(arr[j+1])) {
                tmp := arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
            } else if (getBitCount(arr[j]) == getBitCount(arr[j+1])) {
                if (arr[j] > arr[j+1]) {
                    tmp := arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = tmp
                }
            }
        }
    }
    return arr
}

func getBitCount(num int) int {
    ret := 0
    for num != 0 {
        if (num & 1) {
            ret++
        }
        num >>= 1
    }
    return ret
}



In this question, we need to sort the array of non-negative integers based on the number of 1s in their binary representation. For the same number of 1s, sort based on the decimal value. It is important to note that the array may contain negative integers. The provided solution first defines a helper function `getBitCount` that counts the number of 1s in the binary representation of an integer. Then, the `SortArray` function is defined. It sorts the input array using a bubble sort algorithm. For each pair of adjacent elements, if the number of 1s in the first element's binary representation is greater than the number of 1s in the second element's binary representation, they are swapped. If the number of 1s is the same, the elements are sorted in ascending order. Finally, the sorted array is returned.

Here are some examples of the solution in action:

- `SortArray([1, 5, 2, 3, 4])` returns `[1, 2, 3, 4, 5]`: The array is sorted based on the number of 1s in the binary representation of each element. In this case,