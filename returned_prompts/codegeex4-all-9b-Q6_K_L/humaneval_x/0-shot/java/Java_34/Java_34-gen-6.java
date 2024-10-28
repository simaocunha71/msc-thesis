Here's how you can use a TreeSet to get the unique elements in the list:

```java
public List<Integer> unique(List<Integer> l) {
    Set<Integer> set = new TreeSet<>(l);
    return new ArrayList<>(set);
}
```

The TreeSet class in Java automatically removes duplicates and sorts the elements in ascending order. 

Then, we can create a new ArrayList from the TreeSet to get the list of unique elements in sorted order.