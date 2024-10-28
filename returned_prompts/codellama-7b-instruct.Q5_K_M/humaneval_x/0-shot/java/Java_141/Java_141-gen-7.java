import java.util.*;
import java.lang.*;

class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int n = s.length();
        boolean flag = true;
        for (int i = 0; i < n; i++) {
            if (i == 0) {
                if (!(s.charAt(i) >= 'a' && s.charAt(i) <= 'z' || s.charAt(i) >= 'A' && s.charAt(i) <= 'Z')) {
                    flag = false;
                    break;
                }
            } else if (s.charAt(i) >= '0' && s.charAt(i) <= '9') {
                if (i >= 2) {
                    flag = false;
                    break;
                }
            } else if (s.charAt(i) == '.') {
                if (i == 1 || i == n - 1) {
                    flag = false;
                    break;
                }
            }
        }
        if (flag) {
            if (s.substring(s.indexOf('.') + 1).equals("txt") || s.substring(s.indexOf('.') + 1).equals("exe") || s.substring(s.indexOf('.') + 1).equals("dll")) {
                System.out.println("Yes");
            } else {
                System.out.println("No");
            }
        } else {
            System.out.println("No");
        }
    }
}

