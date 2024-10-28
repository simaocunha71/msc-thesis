    pq := &MinHeap{}
    heap.Init(pq)

    for _, num := range arr {
        heap.Push(pq, num)
        if pq.Len() > k {
            heap.Pop(pq)
        }
    }

    result := make([]int, k)
    for i := k - 1; i >= 0; i-- {
        result[i] = heap.Pop(pq).(int)
    }

    return result
}

type MinHeap []int

func (h MinHeap) Len() int           { return len(h) }
func (h