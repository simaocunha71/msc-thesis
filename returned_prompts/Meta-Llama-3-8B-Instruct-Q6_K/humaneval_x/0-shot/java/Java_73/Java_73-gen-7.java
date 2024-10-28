    public int smallestChange(List<Integer> arr) {
        int n = arr.size();
        List<Integer> arr1 = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            arr1.add(arr.get(n - 1 - i));
        }
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (arr.get(i) != arr1.get(i)) {
                count++;
            }
        }
        return count;
    }
}
