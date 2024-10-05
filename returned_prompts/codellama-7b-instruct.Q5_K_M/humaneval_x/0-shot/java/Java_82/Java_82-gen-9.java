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
        int length = string.length();
        boolean isPrime = false;
        for (int i = 2; i <= length; i++) {
            if (length % i == 0) {
                isPrime = true;
            }
        }
        return isPrime;
    }
}
