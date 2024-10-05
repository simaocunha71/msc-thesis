    public List<Integer> maximum(List<Integer> arr, int k) {
        List<Integer> result = new ArrayList<>();
        // Sort the array in descending order
        Collections.sort(arr, Collections.reverseOrder());
        // Add the maximum k numbers to the result list
        for (int i = 0; i < k; i++) {
            result.add(arr.get(i));
        }
        return result;
    }
}
// Time complexity: O(n log n) due to sorting
// Space complexity: O(k) for the result list
// The sorting is necessary because the problem requires the maximum k numbers, 
// which can't be achieved by simply taking the first k elements of the array. 

