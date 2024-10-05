import java.util.*;
import java.lang.*;

class Solution {
    public Map<String, Integer> histogram(String test) {
        // If the string is empty, return an empty map
        if (test.isEmpty()) {
            return new HashMap<>();
        }

        // Split the string into an array of words
        String[] words = test.split(" ");

        // Create a map to store the frequency of each word
        Map<String, Integer> frequencyMap = new HashMap<>();

        // Iterate over the words and update the frequency map
        for (String word : words) {
            frequencyMap.put(word, frequencyMap.getOrDefault(word, 0) + 1);
        }

        // Find the maximum frequency
        int maxFrequency = 0;
        for (int frequency : frequencyMap.values()) {
            maxFrequency = Math.max(maxFrequency, frequency);
        }

        // Create a map to store the words with the maximum frequency
        Map<String, Integer> result = new HashMap<>();
        for (Map.Entry<String, Integer> entry : frequencyMap.entrySet()) {
            if (entry.getValue() == maxFrequency) {
                result.put(entry.getKey(), entry.getValue());
            }
        }

        return result;
    }
}

class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.println(solution.histogram("a b c")); // {"a": 1, "b": 1, "c": 1}
        System.out.println(solution.histogram("a b b a")); // {"a": 2, "b": 2}
        System.out.println(solution.histogram("a b c a b")); // {"a": 2, "b": 2}
        System.out.println(solution.histogram("b b b b a")); // {"b": 4}
        System.out.println(solution.histogram("")); // {}
    }
}