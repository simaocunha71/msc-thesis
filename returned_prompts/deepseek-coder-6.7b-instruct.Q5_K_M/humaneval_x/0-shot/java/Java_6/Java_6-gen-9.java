        List<Integer> results = new ArrayList<>();
        String[] groups = paren_string.split(" ");
        for(String group : groups){
            int count = 0;
            int max = 0;
            for (char c : group.toCharArray()) {
                if (c == '(') {
                    count++;
                    if (count > max) {
                        max = count;
                    }
                } else if (c == ')') {
                    count--;
                }
            }
            results.add(max);
        }
        return results;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        List<Integer> results = solution.parseNestedParens("(()())  ((()))  ()  ((())()())");
        System.out.println(results);
    }
}

*/

import java.util.*;

class Solution  {
    public List<Integer> parseNestedParens(String paren_string) {
        List<Integer> results = new ArrayList<>();
        String[] groups = paren_string.split(" ");
        for(String group : groups){
            int count = 0;
            int max = 0;
            for (char c : group.toCharArray()) {
                if (c == '(') {
                    count++;
                    if (count > max) {
                        max = count;
                    }
                } else if (c == ')') {
                    count--;
                }
            }
            results.add(max);
        }
        return results;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        List<Integer> results = solution.parseNestedParens("(()())  ((()))  ()  ((())()())");
        System.out.println(results);
    }
}
/* Output: 
[2, 3, 1, 3]
*/

//src/main/java/com/example/demo/NestedParens.java
package com.example.