Here is a simple solution using a HashSet:

```java
public int countDistinctCharacters(String string) {
    Set<Character> set = new HashSet<>();
    for (char c : string.toCharArray()) {
        set.add(Character.toLowerCase(c));
    }
    return set.size();
}
```

This solution works by iterating over each character in the string, converting it to lower case, and then adding it to a HashSet. Since a HashSet does not allow duplicates, this ensures that only distinct characters are counted. The size of the HashSet is then returned as the result.