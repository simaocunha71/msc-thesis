
    var res []int

    for _, num := range l {
        if num > 0 {
            res = append(res, num)
        }
    }

    return res
}

```

## 1.2.4. 정렬

### 1.2.4.1. 버블 정렬

버블 정렬은 가장 간단한 정렬 알고리즘 중 하나로, 리스트의 원소를 비교하여 교환하는 방식으로 정렬을 수행한다. 시간 복잡도는 O(n^2)이다.

```go
