```java
public boolean isSorted(List<Integer> lst) {
    Set<Integer> set = new HashSet<>();
    for (int i = 1; i < lst.size(); i++) {
        if (lst.get(i) < lst.get(i - 1)) {
            return false;
        }
        if (!set.add(lst.get(i))) {
            return false;
        }
    }
    return true;
}
```