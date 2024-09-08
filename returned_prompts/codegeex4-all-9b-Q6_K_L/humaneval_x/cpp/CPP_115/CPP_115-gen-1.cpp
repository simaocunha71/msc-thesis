你的代码中存在几个问题：

1. 在`max_fill`函数中，你试图计算每一行的总和，但实际上，你应该计算每一列的总和，因为每个桶可以取出整列的水。

2. 在计算每一列的总和时，你应该考虑桶的容量。也就是说，如果一列的总和大于桶的容量，你应该将其除以桶的容量并向上取整，因为即使最后一桶不满，也需要计算为一次使用。

3. 在计算桶的使用次数时，你应该考虑每一列的总和除以桶的容量，并向上取整，因为即使最后一桶不满，也需要计算为一次使用。

下面是修改后的代码：

```cpp
#include <stdio.h>
#include <vector>
#include <math.h>
using namespace std;

int max_fill(vector<vector<int>> grid, int capacity) {
    int total = 0;
    for (int j = 0; j < grid[0].size(); j++) {
        int col = 0;
        for (int i = 0; i < grid.size(); i++) {
            col += grid[i][j];
        }
        total += ceil(col / (float)capacity);
    }
    return total;
}

int main() {
    vector<vector<int>> grid = {{0,0,1,0}, {0,1,0,0}, {1,1,1,1}};
    int capacity = 1;
    printf("%d\n", max_fill(grid, capacity));
    return 0;
}
```

这个修改后的代码应该能够正确地计算桶的使用次数。