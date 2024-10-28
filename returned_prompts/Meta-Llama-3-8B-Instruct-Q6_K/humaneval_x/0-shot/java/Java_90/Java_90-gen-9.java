    import java.util.*;

    class Solution {
        public Optional<Integer> nextSmallest(List<Integer> lst) {
            if (lst.isEmpty()) {
                return Optional.empty();
            }
            Integer smallest = lst.get(0);
            Integer secondSmallest = null;
            for (Integer num : lst) {
                if (num < smallest) {
                    secondSmallest = smallest;
                    smallest = num;
                } else if (num < secondSmallest) {
                    secondSmallest = num;
                }
            }
            return secondSmallest != null ? Optional.of(secondSmallest) : Optional.empty();
        }
    }

    // Test the function
    public static void main(String[] args) {
        Solution solution = new Solution();
        List<Integer> lst1 = Arrays.asList(1, 2, 3, 4, 5);
        List<Integer> lst2 = Arrays.asList(5, 1, 4, 3, 2);
        List<Integer> lst3 = new ArrayList<>();
        List<Integer> lst4 = Arrays.asList(1, 1);

        System.out.println(solution.nextSmallest(lst1));  // Optional[2]
        System.out.println(solution.nextSmallest(lst2));  // Optional[2]
        System.out.println(solution.nextSmallest(lst3));  // Optional.empty
        System.out.println(solution.nextSmallest(lst4));  // Optional.empty
    }
}

In this solution, we first check if the list is empty. If it is, we return an empty Optional. Otherwise, we iterate through the list to find the 2nd smallest element. We keep track of the smallest and second smallest elements as we iterate. If we find an element that is smaller than the current smallest, we update the second smallest to the current smallest and the smallest to the new element. If we find an element that is smaller than the current second smallest, we update the second smallest. Finally, we return the second smallest element as an Optional, or an empty Optional if there is no second smallest element.  



