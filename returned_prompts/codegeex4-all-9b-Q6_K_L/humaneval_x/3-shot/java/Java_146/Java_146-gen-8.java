        int count = 0;
        for (int num : nums) {
            if (num > 10 && isOdd(num)) {
                count += 1;
            }
        }
        return count;
    }

    private boolean isOdd(int number) {
        return number % 2 != 0;
    }
}

