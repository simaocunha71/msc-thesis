    sort.Slice(nums, func(i, j int) bool {
        if strconv.Itoa(nums[i]) + strconv.Itoa(nums[j]) < strconv.Itoa(nums[j]) + strconv.Itoa(nums[i]){
            return true
        } else if strconv.Itoa(nums[i]) + strconv.Itoa(nums[j]) == strconv.Itoa(nums[j]) + strconv.Itoa(nums[i]){
            return i < j
        } else{
            return false
        }
    })
    return nums
}



