import java.util.*;
import java.lang.*;

class Solution {
    /**
     * Given a string s, partition s such that every substring of the partition is a palindrome.
     * Return all possible palindrome partitioning of s.
     * For example, given s = "aab",
     * Return
     * [
     *   ["a","a","b"],
     *   ["aa","b"]
     * ]
     */
    public List<List<String>> partition(String s) {
        List<List<String>> ans = new ArrayList<>();
        List<String> l = new ArrayList<>();
        backtrack(s, 0, l, ans);
        return ans;
    }

    public void backtrack(String s, int start, List<String> l, List<List<String>> ans) {
        if (start == s.length()) {
            ans.add(new ArrayList<>(l));
            return;
        }
        for (int i = start; i < s.length(); i++) {
            if (isPalindrome(s.substring(start, i + 1))) {
                l.add(s.substring(start, i + 1));
                backtrack(s, i + 1, l, ans);
                l.remove(l.size() - 1);
            }
        }
    }

    public boolean isPalindrome(String s) {
        int start = 0;
        int end = s.length() - 1;
        while (start < end) {
            if (s.charAt(start) != s.charAt(end))
                return false;
            start++;
            end--;
        }
        return true;
    }
}
