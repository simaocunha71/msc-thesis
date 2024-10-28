        long result = 1;

        for (int i = n; i > 0; i--) {
            result *= i;
        }

        for (int i = n - 1; i > 0; i--) {
            result *= i;
        }

        return result;
    }
}

