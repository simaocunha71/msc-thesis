import java.util.*;
import java.lang.*;

class Solution {
    public List<String> oddCount(List<String> lst) {
        List<String> ans = new ArrayList<String>();
        for (String s : lst) {
            int count = 0;
            for (char c : s.toCharArray()) {
                if ((c - '0') % 2 == 1) count++;
            }
            String t = String.format("the number of odd elements %dn the str%dng %d of the %dnput.", count, count, count, count);
            ans.add(t);
        }
        return ans;
    }
}

class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.oddCount(Arrays.asList("1234567")));
        System.out.println(s.oddCount(Arrays.asList("3","11111111")));
    }
}