        int count = 0;
        for (Integer num : nums) {
            if (Math.abs(num) > 10 &&
                (Math.abs(num) % 10) % 2 != 0 &&
                (Math.abs(num / 10) % 10) % 2 != 0) {
                count++;
            }
        }
        return count;
    }
}

