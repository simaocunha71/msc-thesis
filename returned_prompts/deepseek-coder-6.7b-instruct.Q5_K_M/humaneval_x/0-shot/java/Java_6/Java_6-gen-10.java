        List<Integer> output = new ArrayList<Integer>();
        String[] groups = paren_string.split(" ");
        for(String group: groups){
            int count = 0;
            int max = 0;
            for(int i = 0; i < group.length(); i++){
                if(group.charAt(i) == '('){
                    count++;
                    if(count > max){
                        max = count;
                    }
                }
                else if(group.charAt(i) == ')'){
                    count--;
                }
            }
            output.add(max);
        }
        return output;
    }
}

This program will split the input string into multiple groups, iterate over each character in each group, count the number of open parentheses and update the maximum count. When it encounters a closing parenthesis, it decrements the count. After iterating over all characters in a group, it adds the maximum count to the output list.

The time complexity of this solution is O(n*m) where n is the number of groups and m is the average length of the groups. The space complexity is O(n) for storing the output list.

It is important to note that this solution assumes that the input string is well-formed and does not contain any spaces other than the ones separating the groups.
*/

public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.parseNestedParens("(()()) ((())) () ((())()())"));
    }
}

/*
Output:
[2, 3, 1, 3]
*/