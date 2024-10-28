        Map<String, Integer> map = new HashMap<String, Integer>();
        String[] words = test.split(" ");
        for (String word : words) {
            if (map.containsKey(word)) {
                map.put(word, map.get(word) + 1);
            } else {
                map.put(word, 1);
            }
        }

        int max = Collections.max(map.values());
        Map<String, Integer> result = new HashMap<String, Integer>();
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            if (entry.getValue() == max) {
                result.put(entry.getKey(), entry.getValue());
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.histogram("a b c"));  // Output: {a=1, b=1, c=1}
        System.out.println(solution.histogram("a b b a"));  // Output: {a=2, b=2}
        System.out.println(solution.histogram("a b c a b"));  // Output: {a=2, b=2}
        System.out.println(solution.histogram("b b b b a"));  // Output: {b=4}
        System.out.println(solution.histogram(""));  // Output: {}
    }
}

This solution works by first splitting the input string into a list of words. Then it counts the occurrence of each word in the list and stores them in a HashMap. Finally, it iterates over the HashMap to find the word(s) with the highest occurrence and stores them in another HashMap that is returned.

This solution assumes that the input string is a space-separated sequence of lowercase letters. If the input string contains any uppercase letters, digits, special characters, or spaces in the middle of words, it won't work correctly.
*/

// TC: O(n)
// SC: O(n)

// n is the length of the input