    min_sum := math.MaxInt32
    current_sum := 0

    for _, num := range nums {
        current_sum += num
        min_sum = int(math.Min(float64(min_sum), float64(current_sum)))
        if current_sum < 0 {
            current_sum = 0
        }
    }
    return min_sum
}  // This function returns the minimum sum of any non-empty subarray of nums. It uses Kadane's algorithm to achieve this. The minimum sum is updated at each step. If the current sum becomes negative, it is reset to 0. This ensures that we only consider subarrays that are non-empty.