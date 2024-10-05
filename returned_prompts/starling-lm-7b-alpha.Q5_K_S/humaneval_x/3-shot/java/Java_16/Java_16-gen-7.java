        Set<Character> characters = new HashSet<>();
        for (char c : string.toLowerCase().toCharArray()) {
            characters.add(c);
        }
        return characters.size();
    }
}


public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));
        System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(solution.truncateNumber(3.5));
        System.out.println(solution.countDistinctCharacters("xyzXYZ"));
        System.out.println(solution.countDistinctCharacters("Jerry"));
    }
}
```