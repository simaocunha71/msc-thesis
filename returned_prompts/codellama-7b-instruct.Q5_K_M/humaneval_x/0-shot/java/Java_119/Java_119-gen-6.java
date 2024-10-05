class Solution {
    public String matchParens(List<String> lst) {
        Stack<Character> stk = new Stack<>();
        for (String s : lst) {
            for (char c : s.toCharArray()) {
                if (c == '(') stk.push(c);
                else if (stk.isEmpty() || stk.pop() != '(') return "No";
            }
        }
        return "Yes";
    }
}

B:
public static void main(String[] args) {
        Solution s = new Solution();
        List<String> list = Arrays.asList("()(", ")" );
        System.out.println(s.matchParens(list));
    }

C:
public class Solution {
    public static void main(String[] args) {
        Solution s = new Solution();
        List<String> list = Arrays.asList("()(", ")" );
        System.out.println(s.matchParens(list));
    }

    public String matchParens(List<String> lst) {
        Stack<Character> stk = new Stack<>();
        for (String s : lst) {
            for (char c : s.toCharArray()) {
                if (c == '(') stk.push(c);
                else if (stk.isEmpty() || stk.pop() != '(') return "No";
            }
        }
        return "Yes";
    }
}

D:
public class Solution {
    public static void main(String[] args) {
        Solution s = new Solution();
        List<String> list = Arrays.asList("()(", ")" );
        System.out.println(s.matchParens(list));
    }