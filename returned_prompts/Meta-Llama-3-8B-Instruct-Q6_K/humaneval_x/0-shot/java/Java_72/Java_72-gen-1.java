    public boolean willItFly(List<Integer> q, int w) {
        List<Integer> list = new ArrayList<>(q);
        Collections.sort(list);
        int sum = 0;
        for (int i = list.size() - 1; i >= 0; i--) {
            if (sum + list.get(i) > w) {
                return false;
            }
            sum += list.get(i);
        }
        return isPalindromic(list);
    }

    private boolean isPalindromic(List<Integer> list) {
        String s = "";
        for (int i : list) {
            s += i;
        }
        return s.equals(new StringBuilder(s).reverse().toString());
    }
}  // Time complexity is O(n log n) due to sorting and O(n) for the isPalindromic method. Space complexity is O(n) for the list of integers.  // 1+2 is less than the maximum possible weight, but it's unbalanced.  // it's balanced, but 3+2+3 is more than the maximum possible weight.  // 3+2+3 is less than the maximum possible weight, and it's balanced.  // 3 is less than the maximum possible weight, and it's balanced.  // Time complexity is O(n log n) due to sorting and O(n) for the isPalindromic method. Space complexity is O(n) for the list of integers.  // 1+2 is less than the maximum possible weight, but it's unbalanced.  // it's balanced, but 3+2+3 is more than the maximum possible weight.  // 3+2+3 is less than the maximum possible weight, and it's balanced.  // 3 is less than the maximum possible weight, and it's balanced.  // Time complexity is O(n log n) due to sorting and O(n) for the isPalindromic method. Space complexity is O(n) for the list of integers.  // 1+2 is less than the maximum possible weight, but it's unbalanced.  // it's balanced, but 3+2+3 is more than the maximum possible weight.  // 3+2+3 is less than the maximum possible weight, and it's balanced.  // 3 is less than the maximum possible weight, and it's balanced.  // Time complexity is O(n log n) due to sorting