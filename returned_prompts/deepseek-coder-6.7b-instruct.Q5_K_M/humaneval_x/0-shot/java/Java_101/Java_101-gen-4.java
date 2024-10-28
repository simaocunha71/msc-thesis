        List<String> words = new ArrayList<String>();
        String[] splitWords = s.split("[, ]");
        for(String word : splitWords) {
            if(!word.equals("")) {
                words.add(word);
            }
        }
        return words;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.wordStrings("Hi, my name is John"));
        System.out.println(sol.wordStrings("One, two, three, four, five, six"));
    }
}

This program splits the input string into words based on either comma or space as the delimiter and then adds the words into a list.

Note: This program considers both commas and spaces as delimiters. If you want to consider only one delimiter, you can modify the split method accordingly. For example, if you want to consider only commas as the delimiter, you can replace `[, ]` with `,`.

Also, it assumes that there are no trailing spaces in the input string. If there are trailing spaces, you might want to trim the words before adding them to the list.

This program returns an array of words. If you want to return a different data structure, you can modify the return type of the wordStrings method.

For example, if you want to return a Set instead of a List, you can replace `List<String> words = new ArrayList<String>();` with `Set<String> words = new HashSet<String>();`.
*/

//