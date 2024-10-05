public int canArrange(List<Integer> arr) {
    int maxIndex = -1;
    for (int i = 0; i < arr.size(); i++) {
        if (i < arr.size() - 1 && arr.get(i) >= arr.get(i + 1)) {
            maxIndex = i;
        }
    }
    return maxIndex;
}