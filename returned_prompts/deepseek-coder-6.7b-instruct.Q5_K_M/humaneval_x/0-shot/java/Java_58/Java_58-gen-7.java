        List<Integer> commonList = new ArrayList<>();
        Set<Integer> set = new HashSet<>();
        for(Integer i: l1)
            if(l2.contains(i))
                set.add(i);
        commonList.addAll(set);
        Collections.sort(commonList);
        return commonList;
    }
}

//Test cases:
import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.common(Arrays.asList(1, 4, 3, 34, 653, 2, 5), Arrays.asList(5, 7, 1, 5, 9, 653, 121))); // should print [1, 5, 653]
        System.out.println(sol.common(Arrays.asList(5, 3, 2, 8), Arrays.asList(3, 2))); // should print [2, 3]
    }
}

//This code works by first creating a new HashSet, which can only contain unique elements. It then loops through the first list and checks if each element is also present in the second list. If it is, it adds the element to the HashSet. Finally, it sorts the HashSet into a List and returns it.

//The time complexity of this algorithm is O(n log n) due to the sorting operation, where n is the size of the larger of the two input lists. The space complexity is O(n), as in the worst case scenario, all elements from one list could be in the set.

//This solution assumes that the input lists are sorted, and if they are not, they should be sorted before calling this function.

//This solution also assumes that the input lists do not contain null elements. If the input lists could contain null elements, the function should be modified to handle this case.

//This solution also assumes that the input lists are unmodifiable. If the input lists are modifiable, the function should be modified to prevent unintended modifications to the input lists.

//This solution assumes that the input lists