```java
public boolean rightAngleTriangle(int a, int b, int c) {
    List<Integer> sides = Arrays.asList(a, b, c);
    sides.sort(Comparator.naturalOrder());
    return Math.pow(sides.get(0), 2) + Math.pow(sides.get(1), 2) == Math.pow(sides.get(2), 2);
}
```