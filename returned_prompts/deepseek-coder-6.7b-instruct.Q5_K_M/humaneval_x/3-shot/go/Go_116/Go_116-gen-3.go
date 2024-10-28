    sort.Slice(arr, func(i, j int) bool {
        // count the number of ones in the binary representation of each number
        countI := countOnes(arr[i])
        countJ := countOnes(arr[j])

        // if the counts are equal, compare the decimal values
        if countI == countJ {
            return arr[i] < arr[j]
        }

        return countI < countJ
    })

    return arr
}

func countOnes(n int) int {
    count := 0

    for n > 0 {
        if n%2 == 1 {
            count++
        }

        n /= 2
    }

    return count
}



