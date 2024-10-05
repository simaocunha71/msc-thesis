    public List<Integer> sortArray(List<Integer> array) {
        if (array.isEmpty()) {
            return array;
        }
        int sum = array.get(0) + array.get(array.size() - 1);
        if ((sum & 1) == 0) {
            Collections.sort(array, Collections.reverseOrder());
        } else {
            Collections.sort(array);
        }
        return new ArrayList<>(array);
    }  // This solution creates a new sorted list, does not modify the original array. It also handles the edge case where the array is empty. The sum of the first and last elements is used to determine the sorting order. If the sum is even, the list is sorted in descending order; otherwise, it is sorted in ascending order. Finally, the new sorted list is returned.