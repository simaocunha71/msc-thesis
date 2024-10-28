```java
public int canArrange(List<Integer> arr) {
    int ans = -1;
    for (int i = 1; i < arr.size(); i++) {
        if (arr.get(i) >= arr.get(i - 1)) {
            ans = i;
        }
    }
    return ans;
}
```