import java.util.*;
import java.lang.*;

class Solution {
    /**
     * Write a function that takes a string and returns true if the string
     * length is a prime number or false otherwise
     * Examples
     * primeLength("Hello") == true
     * primeLength("abcdcba") == true
     * primeLength("kittens") == true
     * primeLength("orange") == false
     */
    public boolean primeLength(String string) {

        // Finds the prime numbers between 2 to 10
        int count = 0;
        for (int i = 2; i <= 10; i++) {
            if (i % 2 == 0) {
                continue;
            }
            for (int j = 2; j < i; j++) {
                if (i % j == 0) {
                    count++;
                    break;
                }
            }
            if (count == 0) {
                System.out.println(i);
            }
            count = 0;
        }

        int count1 = 0;
        for (int i = 1; i <= string.length(); i++) {
            if (i % 2 == 0) {
                continue;
            }
            for (int j = 2; j < i; j++) {
                if (i % j == 0) {
                    count1++;
                    break;
                }
            }
            if (count1 == 0) {
                System.out.println(i);
            }
            count1 = 0;
        }
        return (string.length() % 2 == 0) ? false : true;
    }
}