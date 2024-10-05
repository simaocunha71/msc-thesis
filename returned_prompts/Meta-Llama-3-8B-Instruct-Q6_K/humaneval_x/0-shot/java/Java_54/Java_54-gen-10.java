Here is a simple solution in Java. It counts the frequency of each character in both strings and checks if they are equal.

```java
public boolean sameChars(String s0, String s1) {
    if (s0.length() != s1.length()) {
        return false;
    }

    Map<Character, Integer> map0 = new HashMap<>();
    Map<Character, Integer> map1 = new HashMap<>();

    for (char c : s0.toCharArray()) {
        map0.put(c, map0.getOrDefault(c, 0) + 1);
    }

    for (char c : s1.toCharArray()) {
        map1.put(c, map1.getOrDefault(c, 0) + 1);
    }

    return map0.equals(map1);
}
```

This solution has a time complexity of O(n), where n is the length of the strings. It creates two hash maps to store the frequency of each character in both strings, then compares the two maps. If they are equal, it means the strings have the same characters. If not, it returns false. The space complexity is also O(n), as it needs to store the frequency of each character in the hash maps.  }A:  }