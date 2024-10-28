        int result = 0;
        for (int i = 0; i < nums.size(); i++) {
            int n = Math.abs(nums.get(i));
            if (n > 10 && n % 2 != 0 && (n / 10) % 10 % 2 != 0) {
                result += 1;
            }
        }
        return result;
    }
}

