        int result = 0;
        for (int i = 0; i < nums.size(); i++) {
            int number = Math.abs(nums.get(i));
            if (number > 10 && (number % 10) % 2 == 1 && (number / 10) % 10 % 2 == 1) {
                result += 1;
            }
        }
        return result;
    }
}

