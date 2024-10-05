    // Create a copy of the grid to avoid modifying the original one.
    // grid_copy := make([][]int, len(grid))
    // for i := 0; i < len(grid); i++ {
    //     grid_copy[i] = make([]int, len(grid[i]))
    //     for j := 0; j < len(grid[i]); j++ {
    //         grid_copy[i][j] = grid[i][j]
    //     }
    // }

    // Create a priority queue to store the nodes to be explored.
    // var queue []*Node

    // // Add the starting node to the queue.
    // queue = append(queue, &Node{
    //     grid: grid_copy,
    //     value: grid[0][0],
    //     x: 0,
    //     y: 0,
    // })

    // // Visit the queue until there is no more nodes to explore.
    // for len(queue) > 0 {
    //     // Remove the head of the queue.
    //     head := queue[0]
    //     queue = queue[1:]

    //     // If the head has reached the destination, return its value.
    //     if head.x == len(grid)-1 && head.y == len(grid[0])-1 {
    //         return head.value
    //     }

    //     // Add the neighbors of the head to the queue.
    //     for _, neighbor := range head.neighbors() {
    //         queue = append(queue, neighbor)
    //     }
    // }

    // // If the destination cannot be reached, return -1.
    // return -1
}



