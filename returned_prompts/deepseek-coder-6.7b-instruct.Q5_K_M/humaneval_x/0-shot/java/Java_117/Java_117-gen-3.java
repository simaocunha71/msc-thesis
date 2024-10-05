        List<String> words = Arrays.asList(s.split(" "));
        List<String> result = new ArrayList<>();
        for (String word : words) {
            int count = 0;
            for (char c : word.toCharArray()) {
                if (isConsonant(c)) {
                    count++;
                }
            }
            if (count == n) {
                result.add(word);
            }
        }
        return result;
    }

    private boolean isConsonant(char c) {
        c = Character.toLowerCase(c);
        return c >= 'a' && c <= 'z' && c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u';
    }
}

In the function `selectWords`, we split the string s into words and then for each word we count the number of consonants. If the count is equal to n then we add the word to the result list. Finally we return the result list.

The function `isConsonant` checks if a character is a consonant. It converts the character to lower case and checks if it is a letter and not a vowel.

The time complexity of this function is O(n*m) where n is the number of words in the string and m is the length of the longest word. The space complexity is O(n) for storing the words and result list.

Please note that the function `selectWords` assumes that the input string s contains only letters and spaces. If this is not the case, the function will not work correctly.
  
*/

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.selectWords("Mary had a little lamb", 4)); // ["little"]
        System.out.println(solution.selectWords("Mary had a little lamb", 3)); // ["Mary", "lamb"]
        System.out.println(solution.selectWords("simple white space", 2)); // []
        System.out.println(solution.selectWords