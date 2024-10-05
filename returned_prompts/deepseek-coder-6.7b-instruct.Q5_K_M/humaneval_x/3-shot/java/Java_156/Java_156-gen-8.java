        String[] symbols = {"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"};
        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < values.length && number > 0; i++) {
            while (values[i] <= number) {
                number -= values[i];
                result.append(symbols[i]);
            }
        }
        return result.toString();
    }
}

