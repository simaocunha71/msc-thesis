```java
public int maxFill(List<List<Integer>> grid, int capacity) {
    int rows = grid.size();
    int cols = grid.get(0).size();
    int res = 0;
    for (int i = 0; i < rows; i++) {
        int curr = 0;
        for (int j = 0; j < cols; j++) {
            curr += grid.get(i).get(j);
        }
        res += curr / capacity + (curr % capacity > 0 ? 1 : 0);
    }
    return res;
}
```
The solution is a simple iterative solution. It goes through each row of the grid and calculates the total amount of water in that row. Then it calculates how many times the bucket needs to be lowered to extract the water from that row and adds that to the total count. The `curr / capacity` part is for the full buckets and the `curr % capacity > 0 ? 1 : 0` part is for the remaining water in the current row that needs to be extracted in the next iteration. The time complexity is O(m*n), where m is the number of rows and n is the number of columns in the grid. The space complexity is O(1), as it only uses a constant amount of space. 