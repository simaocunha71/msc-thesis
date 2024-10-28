```java
public int add(List<Integer> lst) {
    int total = 0;
    for (int i = 1; i < lst.size(); i += 2) {
        if (lst.get(i) % 2 == 0) {
            total += lst.get(i);
        }
    }
    return total;
}
```