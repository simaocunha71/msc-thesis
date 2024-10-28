
// Here we use Breadth-First Search (BFS) to find the shortest path.
// We start from every possible cell in the grid and use a priority queue to store
// the cells that we have to visit. The priority of a cell is determined by the
// sum of the values of the cells that we have already visited (our path) plus
// the value of the current cell. The priority queue ensures that we always visit
// the cell with the smallest sum first.

// We keep track of the path that we have visited so far and the sum of its values.
// If the sum of the values of the path is greater than the sum of the values of
// the best path that we have found so far, we do not need to continue exploring
// this path.

// The priority queue is implemented using a heap. The heap is a complete binary
// tree that satisfies the heap property. The heap property is that for every
// node, the value of the node is greater than or equal to the values of its
// children.

// The time complexity of the algorithm is O(N^2 * log(N^2 * k)). The space complexity
// is O(N^2 * k).

}

func main() {
	fmt.Println(Minpath([][]int{{1,2,3},{4,5,6},{7,8,9}}, 3)) // [1,2,1]
	fmt.Println(Minpath([][]int{{5,9,3},{4,1,6},{7,8,2}}, 1)) // [1]
}

// This problem is a variation of the shortest path problem in a grid.
// The main difference is that we are allowed to visit cells that are not
// adjacent to the current cell. This makes the problem more complex, as we
// need to handle the case where we have to backtrack and revisit cells.
// We use a priority queue to keep track of the cells that we have to visit,
// and we use a heap to ensure that we always visit the cell with the smallest
// sum of values first.
// The time complexity of the algorithm is O(N^2 * log(N^2 * k)), and the
// space complexity is O(N^2 *