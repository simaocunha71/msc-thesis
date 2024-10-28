```java
public int maxFill(List<List<Integer>> grid, int capacity) {
    int n = grid.size();
    int m = grid.get(0).size();
    int[] heights = new int[n];
    int max_height = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            heights[i] += grid.get(i).get(j);
            max_height = Math.max(max_height, heights[i]);
        }
    }
    int ans = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            int water = heights[i] - grid.get(i).get(j);
            int buckets = (int)Math.ceil((double)water / capacity);
            ans += buckets;
        }
    }
    return ans;
}
```
This solution works by first calculating the height of each well (by summing the water levels in each row), and then calculating the number of buckets needed for each well. The total number of buckets is the sum of the buckets needed for each well.