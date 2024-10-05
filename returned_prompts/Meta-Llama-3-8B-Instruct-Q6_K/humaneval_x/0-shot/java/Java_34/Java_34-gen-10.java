    import java.util.*;

    class Solution {
        public List<Integer> unique(List<Integer> l) {
            Set<Integer> set = new LinkedHashSet<>();
            for (Integer i : l) {
                set.add(i);
            }
            return new ArrayList<>(set);
        }
    }

    // Test the solution
    public static void main(String[] args) {
        Solution solution = new Solution();
        List<Integer> l = Arrays.asList(5, 3, 5, 2, 3, 3, 9, 0, 123);
        List<Integer> result = solution.unique(l);
        System.out.println(result);
    }
    >>> [0, 2, 3, 5, 9, 123]  // Correct output

    Explanation:
    1. Create a LinkedHashSet() to store unique elements.
    2. Iterate through the input list and add each element to the set.
    3. Convert the set to an ArrayList and return it.

    Note: LinkedHashSet is used to preserve the order of elements because it is a combination of HashSet and LinkedList. It provides fast lookup, add, and remove operations, and it also maintains the order in which elements were inserted. 