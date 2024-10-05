

```java
// Convert list to stream and collect to list.
List<Integer> result = numbers.stream()
                             .distinct()
                             .collect(Collectors.toList());

return result;
```


In this code:

- `numbers.stream()`: Returns a stream of the elements in the list.
- `distinct()`: Filters the elements and only keeps those that occur exactly once.
- `collect(Collectors.toList())`: Converts the stream back to a list, keeping the order of the elements intact.

The `distinct()` operation is available in Java 8 and later.

```

```

In Java 7 and earlier, you can achieve the same result as follows:

```java
// Convert list to stream and collect to list.
List<Integer> result = new ArrayList<>();
for (int number : numbers) {
    result.add(number);
}

Collections.sort(result);

Set<Integer> seen = new HashSet<>();
for (int number : result) {
    if (!seen.contains(number)) {
        seen.add(number);
    }
}

result.clear();
result.addAll(seen);
```

```


In this code:

- `new ArrayList<Integer>()`: Creates a new list to store the result.
- `for (int number : numbers) { result.add(number); }`: Adds all the elements from the input list to the result list.
- `Collections.sort(result)`: Sorts the result list.
- `Set<Integer> seen = new HashSet<>();`: Creates a set to store the unique numbers.
- `for (int number : result) {`: Iterates over all the numbers in the result list.
- `if (!seen.contains(number)) {`: If the number is not already in the set, adds it to the set.
- `seen.add(number);`: Adds the number to the set.
- `result.clear();`: Clears the result list.
- `result.addAll(seen);`: Adds all the unique numbers from the set to the result list.