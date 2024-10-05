        int count = 0;
        for (Integer num : nums) {
            if (num > 10 && (num % 10 == 1 || num % 10 == 3 || num % 10 == 5 || num % 10 == 7 || num % 10 == 9)) {
                count += 1;
            }
        }
        return count;
    }
}

