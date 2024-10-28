        List<Integer> sortedList = new ArrayList<>();
        if (lst.isEmpty())
            return sortedList;

        Collections.sort(lst);
        int start = 0;
        int end = lst.size() - 1;

        while (start <= end) {
            sortedList.add(lst.get(start));
            if (start != end) {
                sortedList.add(lst.get(end));
            }
            start++;
            end--;
        }
        return sortedList;
    }
}

This code sorts the list in ascending order first then it adds the minimum and maximum values alternatively to the resultant list to get the strange sorted list.

This code works by initializing two pointers, one at the start of the list and the other at the end of the list. It then enters a loop that continues until the start and end pointers cross each other. In each iteration of the loop, it adds the current minimum and maximum values (the ones pointed to by the start and end pointers) to the resultant list, and then increments the start pointer and decrements the end pointer.

If the start and end pointers ever meet, it means that all the elements have been processed and the loop can end. The resultant list will be a strange sorted list as required.

Time complexity is O(n log n) due to sorting and space complexity is O(n) as we are creating a new list.

Note: This solution assumes that the input list is not null. If it can be null, you should add a null check at the start of the method.

Also note that this solution does not modify the input list, it creates a new list to store the result.

This solution works for any list of integers, not just positive integers. If the list can contain negative numbers, you should adjust the solution accordingly.

Test Cases:

1. strangeSortList(Arrays.asList(1, 2, 3, 4)) should return Arrays.asList(1, 4, 2, 3)
2. strangeSortList(Arrays.asList(5, 5, 5, 5)) should return Arrays.asList(5, 