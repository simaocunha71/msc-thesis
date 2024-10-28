        int n = numbers.size();
        int diff_min = Integer.MAX_VALUE;
        int i_min = 0;
        int j_min = 0;
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                int diff = (int) Math.abs(numbers.get(i) - numbers.get(j));
                if (diff < diff_min) {
                    diff_min = diff;
                    i_min = i;
                    j_min = j;
                }
            }
        }
        return Arrays.asList(numbers.get(i_min), numbers.get(j_min));
    }
}

