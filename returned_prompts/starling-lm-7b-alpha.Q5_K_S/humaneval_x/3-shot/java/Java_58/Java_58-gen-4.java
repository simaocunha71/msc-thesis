        List<Integer> result = new ArrayList<>();
        result.addAll(l1);
        result.retainAll(l2);
        Collections.sort(result);
        return result;
    }
}



public class Practice {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
        System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(solution.truncateNumber(3.5));
        System.out.println(solution.common(Arrays.asList(1, 4, 3, 34, 653, 2, 5), Arrays.asList(5, 7, 1, 5, 9, 653, 121)));
        System.out.println(solution.common(Arrays.asList(5, 3, 2, 8), Arrays.asList(3, 2)));
    }
}

```