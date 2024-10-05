        int count = 0;
        for (int num : nums) {
            int first_digit = num / 100 % 10;
            int last_digit = num % 10;
            if (first_digit % 2 == 0 || last_digit % 2 == 0) continue;
            if (num > 10) count++;
        }
        return count;
    }
}

