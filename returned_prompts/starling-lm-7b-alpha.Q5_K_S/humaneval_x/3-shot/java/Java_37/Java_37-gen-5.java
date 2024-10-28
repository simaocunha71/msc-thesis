        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 2 == 0) {
                result.add(l.get(i));
            } else {
                result.add(l.get(i));
            }
        }
        Collections.sort(result);
        return result;
    }
}


public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        //System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
        //System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));
        //System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));
        //System.out.println(solution.truncateNumber(3.5));
        System.out.println(solution.sortEven(Arrays.asList(5, 6, 3, 4)));
    }
}
```