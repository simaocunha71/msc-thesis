        List<Integer> result = new ArrayList<>();
        for (Integer i : l) {
            if (i % 3 == 0) {
                result.add(Collections.sort(new ArrayList<>(l)));
            } else {
                result.add(i);
            }
        }
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
        //System.out.println(solution.sortThird(Arrays.asList(5, 6, 3, 4, 8, 9, 2)));
    }
}

```