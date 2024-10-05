        int count = 0;

        for (int n : nums) {
            if (n > 10 && ((n / 10) % 2 != 0) && (n % 10) % 2 != 0) {
                count += 1;
            }
        }
        return count;
    }
}

