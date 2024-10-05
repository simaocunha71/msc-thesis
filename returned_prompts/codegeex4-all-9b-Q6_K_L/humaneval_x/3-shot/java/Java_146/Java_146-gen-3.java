        int count = 0;
        for (int num : nums) {
            if (num > 10 && isOdd(num)) count += 1;
        }
        return count;
    }

    private boolean isOdd(int num) {
        int first_digit = num % 10;
        int last_digit = (num / 10) % 10;
        return first_digit % 2 != 0 && last_digit % 2 != 0;
    }
}

