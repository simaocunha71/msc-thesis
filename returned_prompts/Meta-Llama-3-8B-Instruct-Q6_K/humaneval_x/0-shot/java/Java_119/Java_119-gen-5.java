    public String matchParens(List<String> lst) {
        StringBuilder sb = new StringBuilder();
        for(String s : lst) {
            for(char c : s.toCharArray()) {
                if(c == '(') {
                    sb.append('(');
                } else {
                    if(sb.length() == 0 || sb.charAt(sb.length()-1) != '(') {
                        return "No";
                    }
                    sb.deleteCharAt(sb.length()-1);
                }
            }
        }
        return sb.length() == 0 ? "Yes" : "No";
    }

Explanation:
We use a StringBuilder to simulate the stack. When we encounter an open parenthesis, we append it to the StringBuilder. When we encounter a close parenthesis, we check if the StringBuilder is empty or the last character is not an open parenthesis. If it's not, we return "No". If it is, we remove the last character from the StringBuilder. After processing all strings, if the StringBuilder is empty, it means all parentheses are balanced, so we return "Yes". Otherwise, we return "No". 

For example, for the input "()(" and ")"), we process them as follows:
- For "()(", we append '(' to the StringBuilder, resulting in "( ".
- For ")"), we check if the StringBuilder is empty or the last character is not '('. Since it's not, we return "No".

So, the output is "No". 

This solution has a time complexity of O(n), where n is the total number of characters in the input strings. The space complexity is O(n), as in the worst case, we might need to store all characters in the StringBuilder. 







