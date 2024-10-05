
```go

func OrderByPoints(nums []int) []int {
    // Create a slice of struct to hold the number and its sum of digits
    type NumAndSum struct {
        num, sum int
    }
    var numsAndSums []NumAndSum

    for i, num := range nums {
        sum := 0
        // If the number is negative, convert it to positive and calculate the sum of digits
        if num < 0 {
            num = -num
            for num > 0 {
                digit := num % 10
                sum += digit
                num /= 10
            }
            sum = -sum
        } else {
            for num > 0 {
                digit := num % 10
                sum += digit
                num /= 10
            }
        }
        // Append the number and its sum of digits to the slice
        numsAndSums = append(numsAndSums, NumAndSum{i, sum})
    }

    // Sort the slice by the sum of digits in ascending order,
    // and by the index in the original list if there are ties
    sort.Slice(numsAndSums, func(i, j int) bool {
        if numsAndSums[i].sum == numsAndSums[j].sum {
            return numsAndSums[i].num < numsAndSums[j].num
        }
        return numsAndSums[i].sum < numsAndSums[j].sum
    })

    // Create a slice to hold the sorted numbers
    var sortedNums []int
    for _, numAndSum := range numsAndSums {
        // Append the number from the original list at the corresponding index to the sorted numbers slice
        sortedNums = append(sortedNums, nums[numAndSum.num])
    }

    return sortedNums
}
```

```

```go

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

