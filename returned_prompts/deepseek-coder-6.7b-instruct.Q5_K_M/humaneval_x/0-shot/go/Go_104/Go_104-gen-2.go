    var result []int
    for _, num := range x {
        if !hasEvenDigit(num) {
            result = append(result, num)
        }
    }
    sort.Ints(result)
    return result
}

func hasEvenDigit(num int) bool {
    for num > 0 {
        if (num%10)%2 == 0 {
            return true
        }
        num /= 10
    }
    return false
}
```

## 2. 使用Go语言实现的二分查找算法

