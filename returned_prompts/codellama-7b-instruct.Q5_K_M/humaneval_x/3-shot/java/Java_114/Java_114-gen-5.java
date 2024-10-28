        int result = 0, sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            sum += nums.get(i);
            result = Math.min(result, sum);
            if (sum < 0) sum = 0;
        }
        return result;
    }
}

