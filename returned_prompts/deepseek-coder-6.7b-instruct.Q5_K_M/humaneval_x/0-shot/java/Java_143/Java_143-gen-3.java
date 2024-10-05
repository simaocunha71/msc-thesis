        String[] words = sentence.split(" ");
        StringBuilder sb = new StringBuilder();

        for(String word : words){
            if(isPrime(word.length())){
                sb.append(word + " ");
            }
        }

        return sb.toString().trim();
    }

    private boolean isPrime(int num) {
        if(num <= 1) {
            return false;
        }
        for(int i = 2; i*i <= num; i++) {
            if(num % i == 0) {
                return false;
            }
        }
        return true;
    }

}

*/

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        String sentence = "This is a test";
        System.out.println(solution.wordsInSentence(sentence));

        sentence = "lets go for swimming";
        System.out.println(solution.wordsInSentence(sentence));
    }
}

//src/main/java/com/company/easy/StringPalindrome.java
package com.company.easy;

public class StringPalindrome {
    public static void main(String[] args) {
        String str = "madam";
        System.out.println(isPalindrome(str));
    }

    static boolean isPalindrome(String str) {
        int start = 0;
        int end = str.length() - 1;
        while (start < end) {
            if (str.charAt(start) != str.charAt(end)) {
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
}

//src/main/java/com/company/easy/TwoSum.java
package com.company.easy;

import java.util.HashMap;
import java.util.Map;

public class TwoSum {
    public static void main(String[] args) {
        int[] nums = {2, 7