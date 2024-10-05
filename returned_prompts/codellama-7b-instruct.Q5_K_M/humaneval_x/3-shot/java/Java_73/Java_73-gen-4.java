        int min_change = Integer.MAX_VALUE;
        int[] freq = new int[1001];
        for (int x : arr) {
            freq[x] += 1;
        }

        int left = 0;
        int right = arr.size() - 1;
        while (left < right) {
            int x = arr.get(left);
            int y = arr.get(right);

            if (x == y) {
                left += 1;
                right -= 1;
            } else {
                int diff = Math.abs(x - y);
                min_change = Math.min(min_change, diff);
                freq[x] -= 1;
                freq[y] -= 1;
                if (freq[x] > 0) {
                    freq[x] -= 1;
                } else {
                    freq[y] -= 1;
                }
                left += 1;
                right -= 1;
            }
        }
        return min_change;
    }
}

