        String[] roman_digits = {"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"};
        int[] roman_values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};

        String roman_string = "";
        for (int i = 0; i < roman_digits.length; i++) {
            while (number >= roman_values[i]) {
                roman_string += roman_digits[i];
                number -= roman_values[i];
            }
        }
        return roman_string;
    }
}

