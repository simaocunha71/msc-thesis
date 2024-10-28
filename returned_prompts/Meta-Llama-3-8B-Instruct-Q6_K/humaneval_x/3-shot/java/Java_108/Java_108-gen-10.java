        int count = 0;
        for (int num : arr) {
            int sum = 0;
            int abs_num = Math.abs(num);
            while (abs_num > 0) {
                int digit = abs_num % 10;
                sum += digit;
                abs_num /= 10;
            }
            if (sum > 0) {
                count++;
            }
        }
        return count;
    }
}

