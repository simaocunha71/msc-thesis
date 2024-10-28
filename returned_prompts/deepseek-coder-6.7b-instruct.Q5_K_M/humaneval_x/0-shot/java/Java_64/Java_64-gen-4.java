        int count = 0;
        String lowerCase = s.toLowerCase();
        for(int i = 0; i < s.length(); i++){
            char c = lowerCase.charAt(i);
            if( c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'){
                count++;
            }
            if(c == 'y' && i == s.length()-1){
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.vowelsCount("abcde"));
        System.out.println(s.vowelsCount("ACEDY"));
    }
}

*/

import java.util.*;
import java.lang.*;

class Solution {
    public int vowelsCount(String s) {
        int count = 0;
        String lowerCase = s.toLowerCase();
        for(int i = 0; i < s.length(); i++){
            char c = lowerCase.charAt(i);
            if( c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'){
                count++;
            }
            if(c == 'y' && i == s.length()-1){
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.vowelsCount("abcde"));
        System.out.println(s.vowelsCount("ACEDY"));
    }
}

//src/main/java/com/example/vowelCount/VowelCountApplication.java
package com.example.vowelCount;

import com.example.vowelCount.Solution;

public class VowelCountApplication {

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println