    if len(lst) < 2 {
        return nil
    }

    sort.Ints(lst)

    smallest := math.MaxInt64
    secondSmallest := math.MaxInt64

    for _, v := range lst {
        if v < smallest {
            secondSmallest = smallest
            smallest = v
        } else if v < secondSmallest && v != smallest {
            secondSmallest = v
        }
    }

    if secondSmallest == math.MaxInt64 {
        return nil
    }

    return secondSmallest
}

```

## 2. 코드 설명

나는 주어진 정수 목록에서 2번째로 작은 요소를 반환하는 `NextSmallest()` 함수를 작성했습니다. 

정수 목록의 길이가 2보다 작으면(즉, 요소가 없거나 하나밖에 없으면), 함수는 `nil`을 반환합니다. 

함수는 정수 목록을 오름차순으로 정렬합니다. 

그런 다음 함수는 목록을 순회