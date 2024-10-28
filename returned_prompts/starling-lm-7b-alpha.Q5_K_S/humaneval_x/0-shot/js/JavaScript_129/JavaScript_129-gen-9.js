    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            if (grid[i][j] <= k) {
                yield grid[i][j];
                grid[i][j] = -1;
                if (i < grid.length - 1) {
                    if (grid[i + 1][j] !== -1) {
                        yield grid[i + 1][j];
                        grid[i + 1][j] = -1;
                        continue A;
                    }
                }
                if (j < grid[0].length - 1) {
                    if (grid[i][j + 1] !== -1) {
                        yield grid[i][j + 1];
                        grid[i][j + 1] = -1;
                        continue A;
                    }
                }
            }
        }
    }
};



// Test:
function main() {
    const grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ];
    console.log(
        Array.from(
            minPath(grid, 3)
        )
    );
    // Expected Output: [1, 2, 1]

    const grid2 = [
        [5, 9, 3],
        [4, 1, 6],
        [7, 8, 2]
    ];
    console.log(
        Array.from(
            minPath(grid2, 1)
        )
    );
    // Expected Output: [1]
}

main();

















































































