    import java.util.*;

    class Solution {
        public List<List<Integer>> getRow(List<List<Integer>> lst, int x) {
            List<List<Integer>> result = new ArrayList<>();
            for (int i = 0; i < lst.size(); i++) {
                for (int j = lst.get(i).size() - 1; j >= 0; j--) {
                    if (lst.get(i).get(j) == x) {
                        result.add(Arrays.asList(i, j));
                    }
                }
            }
            Collections.sort(result, (a, b) -> a.get(0) - b.get(0));
            return result;
        }
    }
    // Test the method
    public static void main(String[] args) {
        Solution solution = new Solution();
        List<List<Integer>> lst = Arrays.asList(
                Arrays.asList(1, 2, 3, 4, 5, 6),
                Arrays.asList(1, 2, 3, 4, 1, 6),
                Arrays.asList(1, 2, 3, 4, 5, 1)
        );
        int x = 1;
        List<List<Integer>> result = solution.getRow(lst, x);
        for (List<Integer> list : result) {
            System.out.println(list);
        }
    }
