import (
    "sort"
    "strconv"
)

// Write a function which sorts the given list of integers
// in ascending order according to the sum of their digits.
// Note: if there are several items with similar sum of their digits,
// order them based on their index in original list.
// 
// For example:
// >>> OrderByPoints([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
// >>> OrderByPoints([]) == []
func OrderByPoints(nums []int) []int {
    type point struct {
        num int
        sum int
    }
    pts := make([]point, len(nums))
    for i, num := range nums {
        pts[i] = point{
            num: num,
            sum: sumDigits(num),
        }
    }
    sort.SliceStable(pts, func(i, j int) bool {
        if pts[i].sum == pts[j].sum {
            return pts[i].num < pts[j].num
        }
        return pts[i].sum < pts[j].sum
    })
    return points2ints(pts)
}

func sumDigits(n int) int {
    s := strconv.Itoa(n)
    sum := 0
    for i := range s {
        sum += int(s[i] - '0')
    }
    return sum
}

func points2ints(pts []point) []int {
    nums := make([]int, len(pts))
    for i, pt := range pts {
        nums[i] = pt.num
    }
    return nums
}
