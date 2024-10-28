    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid.length; j++) {
            let curr = grid[i][j];
            if (curr < k) {
                grid[i][j] = -curr;
                continue A;
            }
        }
    }

    let stack = [];
    for (let i = 0; i < grid.length; i++) {
        stack.push({ x: i, y: 0 });
        stack.push({ x: i, y: grid[i].length - 1 });
    }
    for (let j = 1; j < grid.length; j++) {
        stack.push({ x: 0, y: j });
        stack.push({ x: grid.length - 1, y: j });
    }

    let res = [];
    while (stack.length > 0) {
        let { x, y } = stack.pop();
        if (grid[x][y] < 0) {
            res.push(grid[x][y]);
        }
        if (res.length === k) {
            break;
        }
        if (x > 0) {
            stack.push({ x: x - 1, y });
        }
        if (y > 0) {
            stack.push({ x, y: y - 1 });
        }
        if (x < grid.length - 1) {
            stack.push({ x: x + 1, y });
        }
        if (y < grid[0].length - 1) {
            stack.push({ x, y: y + 1 });
        }
    }

    return res.slice(0, k);
};

// Time:  O(n^2 + k)
// Space: O(n^2)

*/

/*
  Given a grid with N rows and N columns (N >= 2) and a positive integer k, 
  each cell of the grid contains a value. Every integer in the range [1, N * N]
  inclusive appears exactly once on the cells of