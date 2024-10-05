    for i := range nums {
        sum := 0
        for j := i; j < len(nums); j++ {
            sum += nums[j]
            if sum < 0 {
                break A
            }
        }
        if sum < 0 {
            continue
        }
        return sum
    }
    return -1
}

// Tests
func TestMinsubarraysum(t *testing.T) {
    type test struct {
        input  []int
        output int
    }
    tests := []test{
        {[]int{2, 3, 4, 1, 2, 4}, 1},
        {[]int{-1, -2, -3}, -6},
    }
    for _, tt := range tests {
        actual := Minsubarraysum(tt.input)
        if actual != tt.output {
            t.Errorf("Minsubarraysum(%v) = %d; expected %d", tt.input, actual, tt.output)
        }
    }
}

// Benchmarks
func BenchmarkMinsubarraysum(b *testing.B) {
    for i := 0; i < b.N; i++ {
        for _, tt := range tests {
            Minsubarraysum(tt.input)
        }
    }
}

// 42. Trapping Rain Water

// Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
// For example,
// Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
// Above is a map after raining scorched earth,
// The above map in a smaller scale would look like this (lines are considered water):
// 0 1 0 2 1 0 1 3 2 1 2 1
// The total amount of water trapped is 6.
func TrappingRainWater(height []int) int {

}

// Tests
func TestTrappingRain