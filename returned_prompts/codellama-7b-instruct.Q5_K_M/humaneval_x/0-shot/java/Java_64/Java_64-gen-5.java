import java.util.*;
import java.lang.*;

class Solution {
    public int vowelsCount(String s) {
        int count = 0;
        for (char ch : s.toCharArray()) {
            if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' || (ch == 'y' && isLastChar(s, ch))) {
                count++;
            }
        }
        return count;
    }

    private boolean isLastChar(String s, char ch) {
        return s.charAt(s.length() - 1) == ch;
    }
}

B:
import java.util.*;
import java.lang.*;

class Solution {
    public int vowelsCount(String s) {
        int count = 0;
        for (char ch : s.toCharArray()) {
            if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' || (ch == 'y' && isLastChar(s, ch))) {
                count++;
            }
        }
        return count;
    }

    private boolean isLastChar(String s, char ch) {
        return s.charAt(s.length() - 1) == ch;
    }
}

C:
import java.util.*;
import java.lang.*;

class Solution {
    public int vowelsCount(String s) {
        int count = 0;
        for (char ch : s.toCharArray()) {
            if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' || (ch == 'y' && isLastChar(s, ch))) {
                count++;
            }
        }
        return count;
    }

    private boolean isLastChar(String s, char ch) {
        return s.charAt(s.length() - 1) == ch;
    }
}
