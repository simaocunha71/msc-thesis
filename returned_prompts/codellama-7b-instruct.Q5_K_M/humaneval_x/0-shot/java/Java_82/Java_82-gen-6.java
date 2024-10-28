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

        int len = string.length();
        boolean prime = true;

        if (len == 0)
            return false;

        for (int i = 2; i < len; i++) {
            if (len % i == 0) {
                prime = false;
                break;
            }
        }

        return prime;
    }
}
