The problem is asking to check if two given strings have the same characters, regardless of their order and frequency. 

Here's a Java solution for the problem:

```java
public boolean sameChars(String s0, String s1) {
    if (s0.length() != s1.length()) {
        return false;
    }
    
    Map<Character, Integer> map = new HashMap<>();
    
    for (char c : s0.toCharArray()) {
        map.put(c, map.getOrDefault(c, 0) + 1);
    }
    
    for (char c : s1.toCharArray()) {
        map.put(c, map.getOrDefault(c, 0) - 1);
    }
    
    for (int count : map.values()) {
        if (count != 0) {
            return false;
        }
    }
    
    return true;
}
```

This solution first checks if the lengths of the two strings are equal. If not, it returns false as they cannot have the same characters. 

Then, it creates a HashMap to store the frequency of each character in the first string. 

Next, it iterates over the second string and decrements the frequency of each character in the map. 

Finally, it checks if the frequency of each character in the map is zero. If not, it returns false as the strings do not have the same characters. 

If the frequency of all characters is zero, it returns true as the strings have the same characters. 

This solution has a time complexity of O(n), where n is the length of the strings, as it needs to iterate over each character in the strings. The space complexity is also O(n), as in the worst case, it needs to store each character in the map. 

This solution works correctly even if the strings contain duplicate characters, as it correctly handles the frequency of each character. 