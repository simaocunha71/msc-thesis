The provided solution is not entirely correct. The issue lies in the decoding part. The decoding function should rotate the characters in each group by one position to the right, not shift them. Here's the corrected version:

```java
class Solution {
    public String decodeCyclic(String s) {
        List<String> groups = new ArrayList<>();
        for (int i = 0; i < s.length(); i += 3) {
            groups.add(s.substring(i, Math.min(i + 3, s.length())));
        }
        StringBuilder decoded = new StringBuilder();
        for (String group : groups) {
            if (group.length() == 3) {
                decoded.append(group.charAt(2)).append(group.charAt(0)).append(group.charAt(1));
            } else {
                decoded.append(group);
            }
        }
        return decoded.toString();
    }
}
```

In the decodeCyclic function, for each group of three characters, we check if the length is 3. If it is, we rotate the characters by one position to the right. If the length is less than 3, we simply append the group as it is. The decoded string is then constructed by concatenating the decoded groups.