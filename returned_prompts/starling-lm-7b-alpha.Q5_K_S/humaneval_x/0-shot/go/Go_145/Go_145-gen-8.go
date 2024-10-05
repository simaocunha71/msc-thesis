    // Sort by sum of digits, then by original index.
    type point struct {
        val  int
        idx  int
        sum  int
    }
    numsMap := make(map[int]point)
    for i, v := range nums {
        numsMap[v] = point{idx: i, val: v, sum: sumOfDigits(v)}
    }
    sort.Slice(nums, func(i, j int) bool {
        if numsMap[nums[i]].sum == numsMap[nums[j]].sum {
            return numsMap[nums[i]].idx < numsMap[nums[j]].idx
        }
        return numsMap[nums[i]].sum < numsMap[nums[j]].sum
    })
    return nums

func sumOfDigits(num int) int {
    sum := 0
    for num != 0 {
        sum += num % 10
        num /= 10
    }
    return sum
}

func OrderByPoints(nums []int) []int {
    type point struct {
        val  int
        idx  int
        sum  int
    }
    numsMap := make(map[int]point)
    for i, v := range nums {
        numsMap[v] = point{idx: i, val: v, sum: sumOfDigits(v)}
    }
    sort.Slice(nums, func(i, j int) bool {
        if numsMap[nums[i]].sum == numsMap[nums[j]].sum {
            return numsMap[nums[i]].idx < numsMap[nums[j]].idx
        }
        return numsMap[nums[i]].sum < numsMap[nums[j]].sum
    })
    return nums
}

func sumOfDigits(num int) int {
    sum := 0
    for num != 0 {
        sum += num % 10
        num /= 10
    }
    return sum
