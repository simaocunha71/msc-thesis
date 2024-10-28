        int result = Integer.MAX_VALUE;
        int sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            sum += nums.get(i);
            for (int j = i; j < nums.size(); j++) {
                result = Math.min(result, sum);
                sum -= nums.get(j);
            }
        }
        return result;
    }
}


