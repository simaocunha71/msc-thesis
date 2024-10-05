You can check if a list is monotonic by comparing each element with the next one. If all elements are either increasing or decreasing, then the list is monotonic. Here is the Java code for the same:

```java
public boolean monotonic(List<Integer> l) {
    boolean increasing = true;
    boolean decreasing = true;

    for (int i = 0; i < l.size() - 1; i++) {
        if (l.get(i) < l.get(i + 1)) {
            decreasing = false;
        } else if (l.get(i) > l.get(i + 1)) {
            increasing = false;
        }
    }

    return increasing || decreasing;
}
```

In this code, we initialize two boolean variables `increasing` and `decreasing` to true. As we iterate through the list, we update these variables based on the comparison of each element with the next one. If we find that the list is not increasing or decreasing, we set the respective boolean variable to false. Finally, we return true if either `increasing` or `decreasing` is still true, indicating that the list is monotonic.