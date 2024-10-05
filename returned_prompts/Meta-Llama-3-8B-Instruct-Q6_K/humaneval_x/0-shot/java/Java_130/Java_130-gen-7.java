    public List<Integer> tri(int n) {
        List<Integer> result = new ArrayList<>();
        if (n == 0) {
            result.add(1);
            return result;
        }
        if (n == 1) {
            result.add(1);
            result.add(3);
            return result;
        }
        if (n == 2) {
            result.add(1);
            result.add(3);
            result.add(2);
            return result;
        }

        result.add(1);
        result.add(3);

        int even = 2;
        int odd = 3;
        for (int i = 3; i <= n; i++) {
            if (i % 2 == 0) {
                result.add(even);
                even = (int) (even * 0.5);
            } else {
                int temp = even;
                even = odd;
                odd = temp + odd;
            }
        }
        return result;
    }