    public List<Integer> strangeSortList(List<Integer> lst) {
        List<Integer> result = new ArrayList<>();
        List<Integer> temp = new ArrayList<>();
        temp.addAll(lst);

        while (!temp.isEmpty()) {
            int min = Collections.min(temp);
            temp.remove((Integer) min);
            result.add(min);

            if (!temp.isEmpty()) {
                int max = Collections.max(temp);
                temp.remove((Integer) max);
                result.add(max);
            }
        }

        return result;
    }  // Strange sorting algorithm. It first selects the minimum element from the list, then the maximum, then the minimum and so on. If the list has an odd number of elements, the last element is the minimum.
    // This algorithm is implemented using a temporary list to store the remaining elements after each selection. The algorithm continues until the temporary list is empty. The result list is updated with the selected elements. This algorithm ensures that the elements are in the strange order as described in the problem statement.

    // The time complexity of this algorithm is O(n log n) in the worst case, where n is the number of elements in the input list. This is because the algorithm uses the Collections.min and Collections.max methods, which have a time complexity of O(n log n) in the worst case. The algorithm also uses the remove method, which has a time complexity of O(n) in the worst case. However, the remove method is called only a constant number of times, so its time complexity does not affect the overall time complexity of the algorithm.

    // The space complexity of this algorithm is O(n), where n is the number of elements in the input list. This is because the algorithm uses a temporary list to store the remaining elements after each selection. The temporary list can grow up to a maximum size of n in the worst case. However, the algorithm also uses the result list to store the selected elements, and the result list can grow up to a maximum size of n in the worst case. Therefore, the overall space complexity of the algorithm is O(n).  // Strange sorting algorithm. It first selects the minimum element from the list, then the maximum, then the minimum and so on. If the list has an odd number of elements, the last element is the minimum.
    // This algorithm is implemented using a temporary list to store the remaining elements after each selection. The algorithm continues until the temporary list is empty. The result list is updated with the selected elements. This algorithm ensures that the elements are in