```java
    public int maxFill(List<List<Integer>> grid, int capacity) {
        int ans = 0;
        int rows = grid.size();
        int cols = grid.get(0).size();

        for (int i = 0; i < rows; i++) {
            int sum = 0;
            for (int j = 0; j < cols; j++) {
                sum += grid.get(i).get(j);
            }
            ans += (sum + capacity - 1) / capacity;
        }

        return ans;
    }
```