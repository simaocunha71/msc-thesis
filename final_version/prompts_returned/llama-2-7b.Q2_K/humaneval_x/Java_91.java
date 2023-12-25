import java.util.*;
import java.lang.*;

class Solution {
    /**
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.

    For example:
    >>> isBored("Hello world")
    0
    >>> isBored("The sky is blue. The sun is shining. I love this weather")
    1
     */
    public int isBored(String S) {
        //Write your Solution here
        Map<Character, Integer> boring = new HashMap<Character, Integer>();
        for (int i = 0; i < S.length(); i++) {
            char currChar = S.charAt(i);
            if ((currChar == '.') || (currChar == '?')){
                continue;
            }
            else if (isBoringWord(S, currChar) > 0){
               boring.put((char)currChar, isBoringWord(S, currChar));
            }
        }

        for (Character ch : boring.keySet()) {
            isBored(ch);
        }
        return 0;
    }

    private boolean isBoringWord(String str, char currChar) {
        if ((str == null) || (currChar == '\0')){
           return false;
        }
        else if (isLetter(str.toLowerCase().charAt(0))) {
            if (!isLetter(currChar)){
                isBoringWord(str, str.toLowerCase().charAt(0));
            }
        }
        return false;
    }

   private boolean isLetter (final char ch){
       final int ASCII_NUMERICAL_ORDER[] = {'A', 'B', 'C' , 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T','U', 'V', 'W', 'X', 'Y