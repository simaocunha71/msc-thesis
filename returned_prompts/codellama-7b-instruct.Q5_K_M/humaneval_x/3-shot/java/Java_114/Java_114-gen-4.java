        int result = Integer.MAX_VALUE;

        for (int i = 0; i < nums.size(); i++) {
            int sum = 0;
            for (int j = i; j < nums.size(); j++) {
                sum += nums.get(j);
                result = Math.min(result, sum);
            }
        }
        return result;
    }
}

