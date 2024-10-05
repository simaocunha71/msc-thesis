import java.util.*;
import java.lang.*;

class Solution {
    /**
    Write a function that takes a string and returns true if the string
    length is a prime number or false otherwise
    Examples
    primeLength("Hello") == true
    primeLength("abcdcba") == true
    primeLength("kittens") == true
    primeLength("orange") == false
     */
    public boolean primeLength(String string) {
        int stringLength = string.length();
        int count = 0;
        for (int i = 1; i <= stringLength; i++) {
            if (stringLength % i == 0) {
                count++;
            }
            if (count == 2) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        String[] tests = { "Hello", "abcdcba", "kittens", "orange" };
        for (String s : tests) {
            System.out.println(s + " - " + primeLength(s));
        }
    }
}
