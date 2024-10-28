        int count = 0;
        // Start with the first n-digit number
        for (int i = 1; i < (int)Math.pow(10, n); i++) {
            // Check if the number starts with 1
            if (String.valueOf(i).startsWith("1")) {
                count++;
            }
            // Check if the number ends with 1
            if (String.valueOf(i).endsWith("1")) {
                count++;
            }
        }
        return count;
    }
}

C:
public class Solution {
    public int startsOneEnds(int n) {
        int count = 0;
        for (int i = 1; i < (int)Math.pow(10, n); i++) {
            if (String.valueOf(i).startsWith("1") || String.valueOf(i).endsWith("1")) {
                count++;
            }
        }
        return count;
    }
}

S:
public class Solution {
    public int startsOneEnds(int n) {
        int count = 0;
        for (int i = 1; i < (int)Math.pow(10, n); i++) {
            String str = String.valueOf(i);
            if (str.startsWith("1") || str.endsWith("1")) {
                count++;
            }
        }
        return count;
    }
}

P:
public class Solution {
    public int startsOneEnds(int n) {
        int count = 0;
        for (int i = 1; i < (int)Math.pow(10, n); i++) {
            String s = String.valueOf(i);
            if (s.startsWith("1") || s.endsWith("1")) {
                count++;
            }
        }
        return count;
    }
}

O:
public class Solution {
    public int startsOneEnds(int n) {
        int count = 0;
        for (int i = 1; i < (int)Math.pow(10, n); i++) {
            String s = String.valueOf(i);
            if (s.startsWith("1") || s.endsWith("1")) {
                count++;
            }
        }
        return count;
    }
}

R:
public class Solution {
    public int startsOneEnds(int n) {
        int count = 0;
        for (int i = 1; i < (int)Math.pow(10, n); i++) {
            String s = String.valueOf(i);
            if (s.startsWith("1") || s.endsWith("1")) {
                count++;
