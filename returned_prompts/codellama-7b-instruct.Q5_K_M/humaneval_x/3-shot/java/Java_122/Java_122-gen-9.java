        int result = 0;
        int max = k;
        int min = 1;

        while (min <= max) {
            int mid = (min + max) / 2;
            int sum = 0;
            for (int i = 0; i < mid; i++) {
                sum += arr.get(i);
            }
            if (sum <= 100) {
                if (sum > result) result = sum;
                min = mid + 1;
            } else {
                max = mid - 1;
            }
        }
        return result;
    }
}

