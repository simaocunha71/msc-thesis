```java
public boolean pairsSumToZero(List<Integer> l) {
    for (int i = 0; i < l.size() - 1; i++) {
        for (int j = i + 1; j < l.size(); j++) {
            if (l.get(i) + l.get(j) == 0) {
                return true;
            }
        }
    }
    return false;
}
```