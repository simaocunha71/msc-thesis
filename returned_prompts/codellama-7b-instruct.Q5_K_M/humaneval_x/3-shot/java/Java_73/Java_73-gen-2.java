        int[] freq = new int[100000];
        for (int a : arr) {
            freq[a] += 1;
        }

        int min = Integer.MAX_VALUE;
        for (int a : arr) {
            int b = a + 1;
            if (freq[b] > 0) {
                freq[a] -= 1;
                freq[b] -= 1;
                min = Math.min(min, freq[a] + freq[b]);
            }

            b = a - 1;
            if (freq[b] > 0) {
                freq[a] -= 1;
                freq[b] -= 1;
                min = Math.min(min, freq[a] + freq[b]);
            }
        }

        return min;
    }
}

