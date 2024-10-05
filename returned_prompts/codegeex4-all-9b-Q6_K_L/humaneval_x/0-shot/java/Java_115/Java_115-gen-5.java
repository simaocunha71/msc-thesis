```java
public int maxFill(List<List<Integer>> grid, int capacity) {
        int sum = 0;
        for (List<Integer> row : grid) {
            for (int i : row) {
                sum += i;
            }
        }
        return (int) Math.ceil((double) sum / capacity);
    }
```