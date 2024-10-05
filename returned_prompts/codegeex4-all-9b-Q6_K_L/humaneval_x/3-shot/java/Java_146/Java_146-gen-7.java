        int count = 0;
        for (int i = 0; i < nums.size(); i++) {
            int num = nums.get(i);
            if (num > 10 && isOdd(num)) {
                if (isOdd(num / 10) && isOdd(num % 10)) {
                    count++;
                }
            }
        }
        return count;
    }

    private boolean isOdd(int num) {
        return num % 2 != 0;
    }
}

