        List<Integer> result = new ArrayList<>();
        for (char c : string.toCharArray()) {
            if (c == 'o') {
                result.add(4);
            } else if (c == '|') {
                result.add(0);
            } else {
                result.add(1);
            }
        }
        return result;
    }
}

class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(solution.truncateNumber(3.5));
    }
}
```