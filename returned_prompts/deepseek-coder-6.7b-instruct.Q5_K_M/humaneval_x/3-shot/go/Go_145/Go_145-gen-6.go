    sums := make([]int, len(nums))
    for i, num := range nums {
        digitsSum := 0
        for num != 0 {
            digitsSum += int(math.Abs(float64(num % 10)))
            num /= 10
        }
        sums[i] = digitsSum
    }

    type pair struct {
        i int
        v int
    }

    var pairs []pair
    for i, v := range sums {
        pairs = append(pairs, pair{i, v})
    }

    sort.Slice(pairs, func(i, j int) bool {
        if pairs[i].v == pairs[j].v {
            return pairs[i].i < pairs[j].i
        }
        return pairs[i].v < pairs[j].v
    })

    sortedNums := make([]int, len(nums))
    for i, pair := range pairs {
        sortedNums[i] = nums[pair.i]
    }

    return sortedNums
}



