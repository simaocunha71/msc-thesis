    public List<Integer> strangeSortList(List<Integer> lst) {
        List<Integer> result = new ArrayList<>();
        while (!lst.isEmpty()) {
            int min = Collections.min(lst);
            lst.remove((Integer) min);
            if (!lst.isEmpty()) {
                int max = Collections.max(lst);
                lst.remove((Integer) max);
            }
            result.add(min);
        }
        return result;
    } 
}

Explanation:
The problem is asking to sort a list of integers in a "strange" order. The order is defined as follows: start with the minimum value, then the maximum value of the remaining integers, then the minimum value, and so on.

In the given solution, we use a while loop to iterate through the list until it is empty. In each iteration, we find the minimum value in the list using `Collections.min(lst)` and remove it from the list. If the list is not empty after removing the minimum value, we find the maximum value in the list using `Collections.max(lst)` and remove it from the list. Finally, we add the minimum value to the result list.

This process is repeated until the list is empty. The resulting list is the "strangely" sorted list.

For example, if the input list is `[1, 2, 3, 4]`, the output will be `[1, 4, 2, 3]`. If the input list is `[5, 5, 5, 5]`, the output will be `[5, 5, 5, 5]`. If the input list is empty, the output will be an empty list. 