    public List<Integer> maximum(List<Integer> arr, int k) {
        // First, sort the array in descending order
        Collections.sort(arr, Collections.reverseOrder());

        // Then, return a list of the first k elements
        return arr.subList(0, k);
    }