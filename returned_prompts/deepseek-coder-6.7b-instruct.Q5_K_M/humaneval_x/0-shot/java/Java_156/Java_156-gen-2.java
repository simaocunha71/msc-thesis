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

This solution works by creating two parallel arrays: one for the roman numerals and one for the corresponding integer values.
It then loops over the values array, subtracting the current value from the number and appending the corresponding symbol to the result until the value is greater than the number.
This continues until the number is reduced to zero, at which point all the symbols have been appended.

For example, let's take 19:
- The value of 1000 (m) is greater than 19, so we don't subtract it.
- The value of 900 (cm) is greater than 19, so we don't subtract it.
- The value of 500 (d) is greater than 19, so we don't subtract it.
- The value of 400 (cd) is greater than 19, so we don't subtract it.
- The value of 100 (c) is greater than 19, so we don't subtract it.
- The value of 90 (xc) is greater than 19, so we don't subtract it.
- The value of 50 (l) is greater than 19, so we don't subtract it.
- The value of 40 (xl) is greater than 19, so we don't subtract it.
-