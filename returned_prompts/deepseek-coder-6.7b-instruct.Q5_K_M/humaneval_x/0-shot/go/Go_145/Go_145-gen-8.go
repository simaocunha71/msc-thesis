    sort.Slice(nums, func(i, j int) bool {
        sumI := sumDigits(nums[i])
        sumJ := sumDigits(nums[j])

        if sumI == sumJ {
            return i < j
        }

        return sumI < sumJ
    })

    return nums
}

func sumDigits(n int) int {
    sum := 0

    if n < 0 {
        n = -n
    }

    for n != 0 {
        sum += n % 10
        n /= 10
    }

    return sum
}

func main() {
    fmt.Println(OrderByPoints([]int{1, 11, -1, -11, -12}))  // Outputs: [-1 -11 1 -12 11]
    fmt.Println(OrderByPoints([]int{}))  // Outputs: []
}
```

### Rust

```Rust
// Write a function which sorts the given list of integers
// in ascending order according to the sum of their digits.
// Note: if there are several items with similar sum of their digits,
// order them based on their index in original list.
// 
// For example:
// assert_eq![OrderByPoints(vec![1, 11, -1, -11, -12]), vec![1, -11, -1, -12, 11]];
// assert_eq![OrderByPoints(vec![1]), vec![1]];
fn OrderByPoints(mut nums: Vec<i32>) -> Vec<i32> {
    nums.sort_by_key(|&num| sum_digits(num));
    nums
}

fn sum_digits(mut n: i32) -> i32 {
    let mut sum = 0;
    n = n.abs();
    while n > 0 {
        sum += n % 10;
        n /= 10;
    }
    sum
}

