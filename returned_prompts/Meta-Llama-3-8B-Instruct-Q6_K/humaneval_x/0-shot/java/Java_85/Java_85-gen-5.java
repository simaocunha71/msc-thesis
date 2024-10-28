    public int add(List<Integer> lst) {
        int sum = 0;
        for (int i = 0; i < lst.size(); i++) {
            if (i % 2 != 0 && lst.get(i) % 2 == 0) {
                sum += lst.get(i);
            }
        }
        return sum;
    }  // Time Complexity: O(n), Space Complexity: O(1)
}
