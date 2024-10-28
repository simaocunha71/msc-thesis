        String[] words = test.split(" ");
        Map<String, Integer> map = new HashMap<>();
        for (String word : words) {
            if (map.containsKey(word)) {
                map.put(word, map.get(word) + 1);
            } else {
                map.put(word, 1);
            }
        }

        int max = Collections.max(map.values());
        Map<String, Integer> result = new HashMap<>();
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            if (entry.getValue() == max) {
                result.put(entry.getKey(), entry.getValue());
            }
        }
        return result;
    }
}

This program will create a histogram of the input string by counting the occurrence of each word. Then it will return a map containing only the words that have the highest count. 

The split method is used to divide the string into words based on space. Then a loop is used to count the occurrence of each word. Finally, another loop is used to filter the words that have the highest count.

The time complexity of this program is O(n) because it goes through the string once to create the histogram, and once more to find the maximum and filter the words. The space complexity is also O(n) because in the worst case, each word in the string is unique and stored in the map.

This program will work correctly with any string that contains space-separated lowercase letters.
*/


import java.util.*;

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.println(solution.histogram("a b c")); // {"a": 1, "b": 1, "c": 1}
        System.out.println(solution.histogram("a b b a")); // {"a": 2, "b": 2}
        System.out.println(solution.histogram("a b c a b")); // {"a": 2, "b": 2}
        System.out.println(solution.histogram("b b b b a")); // {"