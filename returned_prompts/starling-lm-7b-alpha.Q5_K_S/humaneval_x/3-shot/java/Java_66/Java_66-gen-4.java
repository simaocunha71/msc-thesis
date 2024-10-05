        int result = 0;
        for (int i = 0; i < s.length(); i++) {
            if (Character.isUpperCase(s.charAt(i))) {
                result += s.charAt(i);
            }
        }
        return result;
    }
}



public class _0100_solution {

    public static void main(String[] args) {

        Solution solution = new Solution();
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));
        System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(solution.truncateNumber(3.5));
        System.out.println(solution.digitSum(""));
        System.out.println(solution.digitSum("abAB"));
        System.out.println(solution.digitSum("abcCd"));
        System.out.println(solution.digitSum("helloE"));
        System.out.println(solution.digitSum("woArBld"));
        System.out.println(solution.digitSum("aAaaaXa"));
    }
}
```