        int current_sum = 0;
        int minimum = Integer.MAX_VALUE;

        for (int i = 0; i < nums.size(); i++) {
            current_sum += nums.get(i);
            minimum = Math.min(minimum, current_sum);

            if (current_sum < 0) current_sum = 0;
        }
        return minimum;
    }
}

