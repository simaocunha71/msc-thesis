
```java
List<String> prefixFilteredList = strings.stream()
                                        .filter(string -> string.startsWith(prefix))
                                        .collect(Collectors.toList());
return prefixFilteredList;
```

This function filters the input list of strings only for ones that start with a given prefix. It does so by using the `filter` function from Java Streams API, which takes a predicate function as an argument. The predicate function in this case checks if the string starts with the given prefix. The `collect` function is used to collect all the strings that pass the filtering condition into a new list, which is then returned.

The time complexity of this function is O(n), where n is the number of strings in the input list. This is because all the strings have to be checked against the prefix, one by one. The space complexity of this function is O(n), as it creates a new list to store the filtered strings.

To test the function, you can use the following test cases:

```java
List<String> strings = Arrays.asList("abc", "bcd", "cde", "array");
System.out.println(filterByPrefix(strings, "a")); // prints ["abc", "array"]
```

This will filter the `strings` list only for the strings that start with the letter "a" and print the result.

```java
List<String> strings = Arrays.asList("abc", "bcd", "cde", "array");
System.out.println(filterByPrefix(strings, "")); // prints ["abc", "bcd", "cde", "array"]
```

This will filter the `strings` list for all strings, regardless of whether they start with a specific prefix or not, and print the result.

```java
List<String> strings = Arrays.asList("abc", "bcd", "cde", "array");
System.out.println(filterByPrefix(strings, "z")); // prints []
```

This will filter the `strings` list for strings that start with the letter "z", but since there are no such strings in the list, it will print an empty list.

```java
List<String> strings