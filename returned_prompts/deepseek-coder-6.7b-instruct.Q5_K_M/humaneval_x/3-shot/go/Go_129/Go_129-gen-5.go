    n  := len(grid)
    length  := n * n
    result  := make([]int, k)
    graph  := make([][]int, length+1)
    dist  := make([]int, length+1)
    visited  := make([]bool, length+1)
    heap  := NewHeap()

    for i  := 0; i < n; i++  {
        for j  := 0; j < n; j++  {
            if j  != n - 1  {
                graph[i*n+j+1] = append(graph[i*n+j+1], (i*n+j+2) )
                graph[(i*n+j+1)] = append(graph[(i*n+j+1)], (i*n+j+2) )
            }
            if i  != n - 1  {
                graph[i*n+j+1] = append(graph[i*n+j+1], ((i+1)*n+j+1) )
                graph[(i+1)*n+j+1] = append(graph[(i+1)*n+j+1], (i*n+j+1) )
            }
        }
    }

    for i  := 1; i <= length; i++  {
        dist[i] = math.MaxInt32
    }

    dist[1] = 0
    heap.Push(Tuple{1, 0})

    for heap.Len() > 0  {
        node  := heap.Pop().(Tuple)
        if visited[node.y]  {
            continue
        }
        visited[node.y] = true

        for _, neighbour  := range graph[node.y] {
            alt  := dist[node.y] + grid[node.y/n][node.y%n]
            if alt < dist[neighbour]  {
                dist[neighbour] = alt
                heap.Push(Tuple{neighbour, alt})
            }
        }
    }

    for i