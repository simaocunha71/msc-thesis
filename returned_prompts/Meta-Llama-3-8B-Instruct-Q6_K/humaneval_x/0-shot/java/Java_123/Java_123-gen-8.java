    public List<Integer> getOddCollatz(int n) {
        List<Integer> result = new ArrayList<>();
        while (n != 1) {
            if (n % 2 == 0) {
                n = n / 2;
            } else {
                n = 3 * n + 1;
            }
            if (n % 2 != 0) {
                result.add(n);
            }
        }
        result.add(1);
        Collections.sort(result);
        return result;
    }  // time complexity is O(log n) because it is a Collatz sequence
    // and space complexity is O(n) for the result list.