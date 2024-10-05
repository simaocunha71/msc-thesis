        List<Integer> copy = new ArrayList<>(array);

        int first = copy.get(0);
        int last = copy.get(copy.size() - 1);

        if ((first + last) % 2 == 0) {
            Collections.sort(copy, Collections.reverseOrder());
        } else {
            Collections.sort(copy);
        }
        return copy;
    }
}


public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));
        System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(solution.truncateNumber(3.5));
        System.out.println(solution.sortArray(Arrays.asList(2, 4, 3, 0, 1, 5)));
        System.out.println(solution.sortArray(Arrays.asList(2, 4, 3, 0, 1, 5, 6)));
    }
}
```