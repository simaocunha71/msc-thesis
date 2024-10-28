    var min_sum int = math.MaxInt32
    var sum int = 0
    var i, j int = 0, 0

    for j < len(nums){
        sum += nums[j]
        if j - i < min_sum{
            min_sum = j - i
        }
        for sum < 0{
            sum -= nums[i]
            i += 1
        }
        j += 1
    }
    return min_sum
}



