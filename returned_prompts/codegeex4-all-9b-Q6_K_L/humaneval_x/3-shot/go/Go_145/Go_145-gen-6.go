    numsString := make([]string,0)

    for _, num := range nums{
        numsString = append(numsString, strconv.Itoa(num))
    }

    sort.Slice(numsString, func(i, j int) bool {
        sum_i := 0
        sum_j := 0
        for _, c := range numsString[i]{
            sum_i += int(c - '0')
        }
        for _, c := range numsString[j]{
            sum_j += int(c - '0')
        }
        return sum_i < sum_j
    })

    for i, num := range numsString{
        nums[i], _ = strconv.Atoi(num)
    }

    return nums
}

