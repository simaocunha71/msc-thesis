```java
import java.util.*;

class Solution {
    public String sortNumbers(String numbers) {
        String[] words = numbers.split(" ");
        Map<String, Integer> map = new HashMap<>();
        map.put("zero", 0);
        map.put("one", 1);
        map.put("two", 2);
        map.put("three", 3);
        map.put("four", 4);
        map.put("five", 5);
        map.put("six", 6);
        map.put("seven", 7);
        map.put("eight", 8);
        map.put("nine", 9);
        List<Integer> list = new ArrayList<>();
        for (String word : words) {
            list.add(map.get(word));
        }
        Collections.sort(list);
        StringBuilder sb = new StringBuilder();
        for (int num : list) {
            sb.append(map.entrySet().stream().filter(e -> e.getValue() == num).findFirst().get().getKey()).append(" ");
        }
        return sb.toString().trim();
    }
}
```