
    type pair struct {
        idx, sum int
        num      int
    }

    pairs := make([]pair, len(nums))
    for i, num := range nums {
        sum := sumOfDigits(num)
        pairs[i] = pair{i, sum, num}
    }

    sort.Slice(pairs, func(i, j int) bool {
        if pairs[i].sum != pairs[j].sum {
            return pairs[i].sum < pairs[j].sum
        }
        return pairs[i].idx < pairs[j].idx
    })

    ordered := make([]int, len(nums))
    for i, pair := range pairs {
        ordered[i] = pair.num
    }

    return ordered
}

func sumOfDigits(num int) int {
    sum := 0
    for num != 0 {
        digit := num % 10
        sum += digit
        num /= 10
    }
    return sum
}

```


## Answer:

```go

import  (
  "strconv"
  "sort"
)

type Pair struct {
  Index int
  Sum int
  Value int
}

func OrderByPoints(nums []int) []int {

  if len(nums) == 0 {
    return []int{}
  }
  
  pairs := make([]Pair, len(nums))

  for i, num := range nums {
    sum := 0
    for _, ch := range strconv.Itoa(num) {
      digit, _ := strconv.Atoi(string(ch))
      sum += digit
    }
    pairs[i] = Pair{i, sum, num}
  }

  sort.Slice(pairs, func(i, j int) bool {
    if pairs[i].Sum != pairs[j].Sum {
      return pairs[i].Sum < pairs[j].Sum
    }
    return pairs[i].Index < pairs[j].Index
  })
