public class Solution {
    public boolean sameChars(String s0, String s1) {
        if (s0.length() != s1.length()) {
            return false;
        }
        Map<Character, Integer> map0 = new HashMap<>();
        Map<Character, Integer> map1 = new HashMap<>();
        for (int i = 0; i < s0.length(); i++) {
            char c0 = s0.charAt(i);
            char c1 = s1.charAt(i);
            map0.put(c0, map0.getOrDefault(c0, 0) + 1);
            map1.put(c1, map1.getOrDefault(c1, 0) + 1);
        }
        return map0.equals(map1);
    }
}
```
This Java solution uses two HashMaps to store the frequency of each character in the two strings. It then compares these two maps to determine if the strings have the same characters. If the strings have the same length and the maps are equal, it returns true, otherwise it returns false. This solution has a time complexity of O(n) where n is the length of the strings. The space complexity is also O(n) as it uses two maps to store the frequency of each character. 
The unit tests provided check for various scenarios, including strings with the same characters, strings with different characters, and strings with different lengths. 
Note: The provided unit tests are based on a specific implementation of the sameChars method. This implementation is case-sensitive and does not handle non-ASCII characters. If you need to handle these cases, you may need to modify the implementation. 
For example, you may need to convert the strings to lower case or use a case-insensitive map. You may also need to handle non-ASCII characters by using a more advanced data structure, such as a Trie. 
In this solution, the sameChars method is defined in the Solution class. The method takes two strings, s0 and s1, as input and returns a boolean value indicating whether the strings have the same characters. 
The method first checks if the strings have the same length. If they do not, it immediately returns false. 
Then, it creates two HashMaps, map0 and map1, to store the frequency of each character in the strings. 
It iterates over the characters in the strings, using the charAt method to get the character at each index. 
For each character, it increments the count in the corresponding map. 
Finally, it compares the