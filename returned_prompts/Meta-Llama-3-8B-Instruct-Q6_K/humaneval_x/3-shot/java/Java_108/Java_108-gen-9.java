        int count = 0;
        for (int num : arr) {
            int sum = 0;
            if (num < 0) {
                num = -num;
            }
            while (num > 0) {
                sum += num % 10;
                num /= 10;
            }
            if (sum > 0) {
                count++;
            }
        }
        return count;
    }
}

