    // Sort the list
    sort.Ints(l)

B:
    // Initialize the first value as previous
    prev := l[0]
    i := 1

C:
    // Loop through the rest of the list
    for _, value := range l[1:] {
        // If the current value is not equal to the previous one
        if value != prev {
            // Move the current value to the i-th position and increment i
            l[i] = value
            i++
        }
        // Update the previous value
        prev = value
    }

D:
    // Return the slice of the list up to the i-th position
    return l[:i]
}


func main()  {
    fmt.Println(Unique([]int{5, 3, 5, 2, 3, 3, 9, 0, 123}))
}
```



## 코드 설명
- 정렬이 된 리스트에서 중복되는 값이 없도록 하는 것이기 때문에 우선 리스트를 정렬한다.
- 리스트의 첫번째 값을 prev로 설정한다.
- 리스트