    public List<Integer> sortArray(List<Integer> arr) {
        Collections.sort(arr, (a, b) -> {
            int countA = Integer.toBinaryString(a).replace("0", "").length();
            int countB = Integer.toBinaryString(b).replace("0", "").length();
            if (countA == countB) {
                return Integer.compare(a, b);
            } else {
                return Integer.compare(countA, countB);
            }
        });
        return arr;
    }