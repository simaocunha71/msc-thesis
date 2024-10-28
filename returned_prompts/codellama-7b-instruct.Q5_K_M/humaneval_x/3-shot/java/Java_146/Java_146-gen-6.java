        int result = 0;
        for (int n : nums) {
            if (n > 10 && (n % 10 == 1 || n % 10 == 3 || n % 10 == 5 || n % 10 == 7 || n % 10 == 9)) {
                result += 1;
            }
        }
        return result;
    }
}

