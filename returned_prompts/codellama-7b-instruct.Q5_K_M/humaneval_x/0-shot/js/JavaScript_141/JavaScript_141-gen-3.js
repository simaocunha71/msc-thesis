        int count = 0;
        for (int num : nums) {
            if (num > 10 && ((num % 10 > 1 && num % 10 < 9) || (num % 10 == 1 || num % 10 == 9))) {
                count += 1;
            }
        }
        return count;
    }
}

