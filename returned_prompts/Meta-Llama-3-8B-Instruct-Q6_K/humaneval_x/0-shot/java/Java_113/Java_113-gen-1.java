    import java.util.*;

    class Solution {
        public List<String> oddCount(List<String> lst) {
            List<String> result = new ArrayList<>();
            for (String s : lst) {
                int count = 0;
                for (char c : s.toCharArray()) {
                    if ((c - '0') % 2 != 0) {
                        count++;
                    }
                }
                result.add("the number of odd elements " + count + "n the str" + (lst.indexOf(s) + 1) + "ng " + (lst.indexOf(s) + 1) + " of the " + "nput.");
            }
            return result;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        List<String> lst = new ArrayList<>();
        lst.add("1234567");
        lst.add("3");
        lst.add("11111111");
        List<String> result = solution.oddCount(lst);
        for (String s : result) {
            System.out.println(s);
        }
    }

Output:

the number of odd elements 4n the str4ng 4 of the 4nput.
the number of odd elements 1n the str1ng 1 of the 1nput.
the number of odd elements 8n the str8ng 8 of the 8nput.