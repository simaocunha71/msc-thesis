        if (lst.size() < 2) {
            return Optional.empty();
        }

        int firstMin = Integer.MAX_VALUE;
        int secondMin = Integer.MAX_VALUE;

        for (Integer num : lst) {
            if (num < firstMin) {
                secondMin = firstMin;
                firstMin = num;
            } else if (num < secondMin && num != firstMin) {
                secondMin = num;
            }
        }

        if (secondMin == Integer.MAX_VALUE) {
            return Optional.empty();
        }

        return Optional.of(secondMin);
    }
}

Explanation:
Here, we traverse the list and keep track of the smallest and the second smallest elements. When we find a new smallest element, we update the second smallest element to be the old smallest element, and the smallest element to be the new element. If we find an element that is in between the smallest and the second smallest, we update the second smallest element. At the end of the traversal, the second smallest element is the 2nd smallest element in the list. If there is no such element, the second smallest element remains as Integer.MAX_VALUE, and we return Optional.empty().

Test Cases:

assert(Solution.nextSmallest(Arrays.asList(1, 2, 3, 4, 5)).equals(Optional.of(2)));
assert(Solution.nextSmallest(Arrays.asList(5, 1, 4, 3, 2)).equals(Optional.of(2)));
assert(Solution.nextSmallest(Arrays.asList()).equals(Optional.empty()));
assert(Solution.nextSmallest(Arrays.asList(1, 1)).equals(Optional.empty()));

The problem can be solved in O(n) time complexity where n is the size of the list.

Note: This solution assumes that the list does not contain duplicate elements. If the list can contain duplicate elements, additional checks should be added to handle this case.

Also, the problem statement is a bit ambiguous. The function should return the second smallest distinct element. In the example, the function should return 2 as the second smallest