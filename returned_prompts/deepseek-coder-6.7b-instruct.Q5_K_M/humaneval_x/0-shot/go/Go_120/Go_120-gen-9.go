    h := &IntHeap{}
    for _, v := range arr {
        heap.Push(h, v)
    }
    result := make([]int, k)
    for i := 0; i < k; i++ {
        result[i] = heap.Pop(h).(int)
    }
    return result
}


