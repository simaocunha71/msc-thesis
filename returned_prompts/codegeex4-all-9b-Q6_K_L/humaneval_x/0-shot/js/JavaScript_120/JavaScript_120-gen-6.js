```java
class Solution {
    public int[] maximum(int[] arr, int k) {
        if (k == 0) return new int[0];
        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = arr[i];
        }
        Arrays.sort(result);
        return result;
    }
}
```
