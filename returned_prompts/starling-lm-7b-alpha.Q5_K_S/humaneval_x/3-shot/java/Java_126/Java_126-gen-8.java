        for (int i = 0; i < lst.size() - 1; i++) {
            if (lst.get(i) > lst.get(i + 1)) return false;
        }
        return true;
    }
}


public class Practice {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));
        System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(solution.truncateNumber(3.5));
        System.out.println(solution.isSorted(Arrays.asList(5)));
        System.out.println(solution.isSorted(Arrays.asList(1, 2, 3, 4, 5)));
        System.out.println(solution.isSorted(Arrays.asList(1, 3, 2, 4, 5)));
        System.out.println(solution.isSorted(Arrays.asList(1, 2, 3, 4, 5, 6)));
        System.out.println(solution.isSorted(Arrays.asList(1, 2, 3, 4, 5, 6, 7)));
        System.out.println(solution.isSorted(Arrays.asList(1, 3, 2, 4, 5, 6, 7)));
        System.out.println(solution.isSorted(Arrays.asList(1, 2, 2, 3, 3, 4)));
        System.out.println(solution.isSorted(Arrays.asList(1, 2, 2, 2, 3, 4)));
    }
}