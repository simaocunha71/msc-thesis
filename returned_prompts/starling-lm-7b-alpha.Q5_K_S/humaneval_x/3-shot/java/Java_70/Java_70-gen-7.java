        List<Integer> result = new ArrayList<>();
        List<Integer> copy = new ArrayList<>(lst);
        Collections.sort(copy);
        int min = copy.get(0);

        while (copy.size() > 0) {
            result.add(min);
            int max = Collections.max(new ArrayList<>(copy));
            copy.remove(copy.indexOf(max));
            min = copy.get(0);
        }
        return result;
    }
}

public class CodeChallenges {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));
        System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(solution.truncateNumber(3.5));
        System.out.println(solution.strangeSortList(Arrays.asList(1, 2, 3, 4)));
        System.out.println(solution.strangeSortList(Arrays.asList(5, 5, 5, 5)));
        System.out.println(solution.strangeSortList(Arrays.asList()));
    }
}
```