        int count = 0;
        for (int num : arr) {
            if (num < 0) num = -num;
            int digit_sum = 0;
            while (num > 0) {
                digit_sum += num % 10;
                num /= 10;
            }
            if (digit_sum > 0) count += 1;
        }
        return count;
    }
}

