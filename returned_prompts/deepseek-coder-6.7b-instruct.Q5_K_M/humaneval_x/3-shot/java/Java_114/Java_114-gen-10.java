        int min = Integer.MAX_VALUE, sum = 0;
        for (int num : nums) {
            sum += num;
            min = Math.min(min, sum);
            sum = Math.min(sum, 0);
        }
        return min;
    }
}

