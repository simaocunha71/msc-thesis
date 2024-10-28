        String[] mini_roman = {
                "m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"
        };
        int[] mini_values = {
                1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
        };

        StringBuilder result = new StringBuilder();
        int current = number;

        for (int i = 0; i < mini_values.length && current > 0; i++) {
            while (current >= mini_values[i]) {
                current -= mini_values[i];
                result.append(mini_roman[i]);
            }
        }
        return result.toString();
    }
}

