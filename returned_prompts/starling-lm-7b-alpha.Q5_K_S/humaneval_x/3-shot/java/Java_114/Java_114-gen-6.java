        int min = Integer.MAX_VALUE;
        int prefix = 0;
        for (int i = 0; i < nums.size(); i++) {
            prefix += nums.get(i);
            int suffix = prefix;
            while (i < nums.size() && suffix > 0) {
                min = Math.min(min, suffix);
                suffix -= nums.get(i);
                i++;
            }
            i--;
        }
        return min;
    }
}

