        int count = 0;
        for (int n : nums) {
            if (n > 10 && (n % 10 != 0 && n % 1 == n % 10)) {
                count += 1;
            }
        }
        return count;
    }
}

