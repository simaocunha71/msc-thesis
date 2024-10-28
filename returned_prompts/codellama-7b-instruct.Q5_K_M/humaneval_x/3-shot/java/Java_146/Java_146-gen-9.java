        int count = 0;
        for (int num : nums) {
            if (num > 10 && (num % 10 > 0 && num % 10 < 10 && num % 100 > 10 && num % 100 < 90)) {
                count++;
            }
        }
        return count;
    }
}

