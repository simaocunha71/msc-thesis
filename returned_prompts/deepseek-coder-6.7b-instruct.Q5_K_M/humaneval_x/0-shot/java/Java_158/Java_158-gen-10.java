        String maxWord = "";
        int maxCount = 0;

        for(String word : words) {
            Set<Character> uniqueChars = new HashSet<>();
            for(char c : word.toCharArray()) {
                uniqueChars.add(c);
            }

            if(uniqueChars.size() > maxCount) {
                maxCount = uniqueChars.size();
                maxWord = word;
            } else if(uniqueChars.size() == maxCount) {
                if(word.compareTo(maxWord) < 0) {
                    maxWord = word;
                }
            }
        }

        return maxWord;
    }
}

The solution works by iterating through each word in the list, creating a HashSet for each word containing its unique characters. It then checks if the size of the HashSet is greater than the current maximum count. If it is, it sets the maximum count to the size of the HashSet and the maximum word to the current word. If the size of the HashSet is equal to the maximum count, it checks if the current word is lexicographically smaller than the maximum word. If it is, it sets the maximum word to the current word. Finally, it returns the maximum word.

I hope this helps and happy coding!!
*/

// Your code here along with any other code you'd like to test the solution.

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        List<String> words1 = Arrays.asList("name", "of", "string");
        List<String> words2 = Arrays.asList("name", "enam", "game");
        List<String> words3 = Arrays.asList("aaaaaaa", "bb", "cc");

        System.out.println(solution.findMax(words1));  // "string"
        System.out.println(solution.findMax(words2));  // "enam"
        System.out.println(solution.findMax(words3));  // "aaaaaaa"
    }
}



















