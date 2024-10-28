    public List<Integer> removeDuplicates(List<Integer> numbers) {
        Map<Integer, Boolean> map = new HashMap<>();
        List<Integer> result = new ArrayList<>();
        for (int num : numbers) {
            if (!map.containsKey(num)) {
                map.put(num, true);
                result.add(num);
            }
        }
        return result;
    }  // Time complexity: O(n), Space complexity: O(n) where n is the size of the input list.