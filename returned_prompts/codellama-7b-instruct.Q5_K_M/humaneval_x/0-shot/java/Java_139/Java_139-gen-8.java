        if (n <= 0) {
            return 0;
        } else {
            long result = 1;
            for (int i = n; i >= 1; i--) {
                result *= i;
            }
            return result;
        }
    }
}
