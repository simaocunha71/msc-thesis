  const N = grid.length;
  const distances = new Array(N).fill(0).map(() => new Array(N).fill(Infinity));
  const directions = [[0, 1], [1, 0], [0, -1], [-1, 0]];
  const visited = new Array(N).fill(0).map(() => new Array(N).fill(false));
  const minHeap = new PriorityQueue((a, b) => a[2] - b[2]);
  minHeap.enqueue([0, 0, grid[0][0], []]);
  distances[0][0] = grid[0][0];

  while (!minHeap.isEmpty()) {
    const [x, y, dist, path] = minHeap.dequeue();
    if (dist > distances[x][y]) continue;
    if (x === N - 1 && y === N - 1) return path.slice(1);

    for (const [dx, dy] of directions) {
      const nx = x + dx;
      const ny = y + dy;
      if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
      const ndist = dist + grid[nx][ny];
      if (ndist < distances[nx][ny]) {
        distances[nx][ny] = ndist;
        minHeap.enqueue([nx, ny, ndist, [...path, grid[nx][ny]]]);
      }
    }
  }

  return [];
}

class PriorityQueue {
  constructor(comparator) {
    this.data = [];
    this.comparator = comparator;
  }

  enqueue(element) {
    this.data.push(element);
    this.data.sort(this.comparator);
  }

  dequeue() {
    return this.data.shift();
  }

  isEmpty() {
    return this.data.length === 0;
  }
}