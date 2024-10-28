    return grid.size();
}

int main(){
    vector<vector<int>> grid={{0,0,1,0},{0,1,0,0},{1,1,1,1}};
    int capacity=1;
    printf("%d",max_fill(grid,capacity));
    return 0;
}

//Output: 3

// This is because the grid has 3 rows, so you need to empty the buckets 3 times to empty all the wells.

// So, the answer is 3.

// Thus, the complexity of this solution is O(n) where n is the total number of wells (rows in the grid).
// As you can see, we have reduced the problem to a simpler one by simply returning the number of rows in the grid.
// This is a common technique in competitive programming known as reducing the problem to a simpler one.
// This is a simple and efficient solution.
