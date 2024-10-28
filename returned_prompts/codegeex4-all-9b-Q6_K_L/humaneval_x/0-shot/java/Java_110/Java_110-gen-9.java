```java
public String exchange(List<Integer> lst1, List<Integer> lst2) {
    int odd = 0;
    for (int i : lst1) {
        if (i % 2 != 0) {
            odd++;
        }
    }
    for (int i : lst2) {
        if (i % 2 == 0) {
            odd--;
        }
    }
    return odd <= 0 ? "YES" : "NO";
}
```