        if (strings.isEmpty())
            return Optional.empty();

        String longest = strings.get(0);
        for (String string : strings) {
            if (string.length() > longest.length()) {
                longest = string;
            }
        }
        return Optional.of(longest);
    }
}


A: You're on the right track, but the question states that you should return the first longest string in case of a tie. You just need to modify the for loop to return the first longest string as soon as it's found:

public Optional<String> longest(List<String> strings) {
    if (strings.isEmpty())
        return Optional.empty();

    for (String string : strings) {
        if (string.length() == strings.get(0).length())
            return Optional.of(string);
    }

    return Optional.of(strings.get(0));
}

This code will return the first longest string in case of a tie, and if there's only one string in the list, it will return that string. If the list is empty, it will return an Optional.empty().

A: You're on the right track. Here is the modified code which returns the first longest string in case of a tie:

```java
public Optional<String> longest(List<String> strings) {
    if (strings.isEmpty())
        return Optional.empty();

    String longest = strings.get(0);
    for (String string : strings) {
        if (string.length() >= longest.length()) {
            longest = string;
        }
    }
    return Optional.of(longest);
}
```

This code will return the first longest string in case of a tie, and if there's only one string in the list, it will return that string. If the list is empty, it will return an Optional.empty().

A: Also, you can use Java 8's Stream API to find the longest string:

```java
public Optional<String> longest(List<String> strings) {
    return strings.stream().max(Comparator.comparing(String::length));
}
```

This code uses the `stream()