    sort.Slice(arr, func(i, j int) bool {
        // convert to binary and count ones
        countOnesI := countOnes(arr[i])
        countOnesJ := countOnes(arr[j])

        // if counts are equal, compare decimal values
        if countOnesI == countOnesJ {
            return arr[i] < arr[j]
        }

        return countOnesI < countOnesJ
    })

    return arr
}

func countOnes(num int) int {
    count := 0
    for num > 0 {
        if num%2 == 1 {
            count++
        }
        num /= 2
    }
    return count
}



