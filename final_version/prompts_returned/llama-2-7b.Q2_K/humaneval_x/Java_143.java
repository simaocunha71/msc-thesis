import java.util.*;
import java.lang.*;

class Solution {
    /**
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
     */
    public String wordsInSentence(String sentence) {
        // Your code here
        StringBuilder sb = new StringBuilder();
        List<String> list_str = new ArrayList<>();
        // 把这个字符串分成单词和空格
        for (int i = 0; i < sentence.length(); i++) {
            char c = sentence.charAt(i);
            if (!Character.isLetterOrDigit(c)) {
                list_str.add(sentence.substring(i, i + 1));
                break;
            } else {
                sb.append(' ').append(list_str.get(i - 1));
                list_str.remove(list_str.size() - 1);
            }
        }
        if (list_str.isEmpty()) {
            return sentence;
        } else {
            Collections.sort(list_str, new Comparator<String>() {
                @Override
                public int compare(String o1, String o2) {
                    return Integer.valueOf(o1).intValue() - Integer.valueOf(o2).intValue();
                }
            });
        }
        sb.append(' ');
        for (Iterator<String> itr = list_str.iterator(); itr.hasNext(); ) {
            String str = itr.next();
            sb.append(str + " ");
            if (sb.length()