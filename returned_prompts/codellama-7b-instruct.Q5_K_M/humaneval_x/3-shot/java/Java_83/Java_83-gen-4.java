        int result = 0;
        int num_digits = (int) Math.pow(10, n - 1);

        for (int i = 1; i <= num_digits; i++) {
            String str = String.valueOf(i);
            if (str.startsWith("1") || str.endsWith("1")) {
                result += 1;
            }
        }
        return result;
    }
}

