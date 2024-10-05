        List<Integer> ans = new ArrayList<>(Arrays.asList(0, 0));
        for (int i = 1; i <= n; i++) {
            if (isPalindrome(i)) {
                if (i % 2 == 0) {
                    ans.set(0, ans.get(0) + 1);
                } else {
                    ans.set(1, ans.get(1) + 1);
                }
            }
        }
        return ans;
    }

    private boolean isPalindrome(int n) {
        String str = String.valueOf(n);
        int i = 0, j = str.length() - 1;
        while (i < j) {
            if (str.charAt(i) != str.charAt(j)) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}

*/

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

        int n = 12;
        System.out.println(sol.evenOddPalindrome(n));
    }
}


A: You can use a HashMap to store the count of even and odd palindrome numbers. Then iterate through the numbers from 1 to n, and for each number, check if it's a palindrome and then increment the corresponding count in the map.

Here is the Java solution:

```java
import java.util.*;

class Solution {
    public List<Integer> evenOddPalindrome(int n) {
        Map<String, Integer> countMap = new HashMap<>();
        countMap.put("even", 0);
        countMap.put("odd", 0);
        
        for(int i = 1; i <= n; i++){
            if(isPalindrome(i)){
                if(i % 2 == 0)
                    countMap.put("even", countMap.get("even") + 1);
                else
                    countMap.put("odd", countMap.get("odd