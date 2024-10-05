        for (int i = 0; i < a.length(); i++) {
            for (int j = 0; j < b.length(); j++) {
                String temp = b.substring(j);
                if (a.contains(temp)) {
                    return true;
                }
            }
        }
        return false;

    }
}


B:
import java.util.*;
import java.lang.*;

class Solution {
    public boolean cycpatternCheck(String a, String b) {
        if (a.length() < b.length()) {
            return false;
        }
        for (int i = 0; i < b.length(); i++) {
            char[] arr = b.toCharArray();
            for (int j = 0; j < arr.length; j++) {
                arr[j] = (char) (arr[j] + 1);
            }
            if (a.contains(new String(arr))) {
                return true;
            }
        }
        return false;
    }
}


C:
import java.util.*;
import java.lang.*;

class Solution {
    public boolean cycpatternCheck(String a, String b) {
        char[] ca = a.toCharArray();
        char[] cb = b.toCharArray();
        int i = 0;
        int j = 0;
        while (i < ca.length && j < cb.length) {
            if (ca[i] == cb[j]) {
                i++;
                j++;
            } else {
                cb[j] = (char) (cb[j] + 1);
                j = 0;
            }
        }
        return i == ca.length;
    }
}


D:
import java.util.*;
import java.lang.*;

class Solution {
    public boolean cycpatternCheck(String a, String b) {
        int i = 0;
        int j = 0;
        while (i < a.length() && j < b.length()) {
            if (a.charAt(i) == b.charAt(j)) {