Here is a simple Java solution using a HashSet to keep track of distinct characters:

```java
public int countDistinctCharacters(String string) {
    Set<Character> distinctChars = new HashSet<>();
    for (char c : string.toCharArray()) {
        distinctChars.add(Character.toLowerCase(c));
    }
    return distinctChars.size();
}
```

This code works by iterating over each character in the string, converting it to lower case and adding it to a HashSet. Since a HashSet only allows distinct elements, any duplicates will be automatically removed. Finally, the size of the HashSet is returned, which is the number of distinct characters in the string.