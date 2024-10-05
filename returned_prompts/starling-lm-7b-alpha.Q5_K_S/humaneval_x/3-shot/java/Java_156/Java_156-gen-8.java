        String[] numerals = {
            "m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"
        };
        int[] values = {
            1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
        };

        String result = "";
        for (int i = 0; i < values.length; i++) {
            while (number >= values[i]) {
                result += numerals[i];
                number -= values[i];
            }
        }
        return result;
    }
}

