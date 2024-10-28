    public boolean pairsSumToZero(List<Integer> l) {
        Set<Integer> numSet = new HashSet<>();
        for (int num : l) {
            if (numSet.contains(-num)) {
                return true;
            }
            numSet.add(num);
        }
        return false;
    }
    // Example usage:
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.pairsSumToZero(Arrays.asList(1, 2, 3, 7))); // Output: false
        System.out.println(solution.pairsSumToZero(Arrays.asList(2, 4, -5, 3, 5, 7))); // Output: true
        System.out.println(solution.pairsSumToZero(Arrays.asList(1))); // Output: false
    }
