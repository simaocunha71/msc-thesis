import java.util.*;
import java.lang.*;

class Solution {
    public String encrypt(String s) {
        String encrypted = "";
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c >= 'a' && c <= 'z') {
                c += 2 * 2;
            } else if (c >= 'A' && c <= 'Z') {
                c += 2 * 2;
            }
            encrypted += c;
        }
        return encrypted;
    }
}

B:
import java.util.*;
import java.lang.*;

class Solution {
    public String encrypt(String s) {
        String encrypted = "";
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c >= 'a' && c <= 'z') {
                c += 2 * 2;
            } else if (c >= 'A' && c <= 'Z') {
                c += 2 * 2;
            }
            encrypted += c;
        }
        return encrypted;
    }
}

C:
import java.util.*;
import java.lang.*;

class Solution {
    public String encrypt(String s) {
        String encrypted = "";
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c >= 'a' && c <= 'z') {
                c += 2 * 2;
            } else if (c >= 'A' && c <= 'Z') {
                c += 2 * 2;
            }
            encrypted += c;
        }
        return encrypted;
    }
}