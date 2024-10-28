        StringBuilder sb = new StringBuilder();
        for (char ch : s.toCharArray()) {
            sb.append((char) ('a' + ((ch - 5) % 26)));
        }
        return sb.toString();
    }
}



public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
        System.out.println(sol.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));
        System.out.println(sol.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(sol.truncateNumber(3.5));
        System.out.println(sol.encodeShift("hello"));
        System.out.println(sol.decodeShift("mjqqt"));
    }
}
```