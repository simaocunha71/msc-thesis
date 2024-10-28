        StringBuilder result = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (c >= 'a' && c <= 'z') {
                result.append((char)(c - 'a' + 'A'));
            } else if (c >= 'A' && c <= 'Z') {
                result.append((char)(c + 'a' - 'A'));
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }
}



public class ProblemSolving {
    public static void main(String[] args) {

        Solution solution = new Solution();
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));
        System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(solution.truncateNumber(3.5));
        System.out.println(solution.encode("test"));
        System.out.println(solution.encode("This is a message"));


    }
}
```