        String[] mini_roman_nums = new String[] { "i", "iv", "v", "ix", "x", "xl", "l", "xc", "c", "cd", "d", "cm", "m" };
        int[] mini_roman_vals = new int[] { 1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000 };

        StringBuilder result = new StringBuilder();

        while (number > 0) {
            for (int i = 0; i < mini_roman_vals.length; i++) {
                if (number >= mini_roman_vals[i]) {
                    result.append(mini_roman_nums[i]);
                    number -= mini_roman_vals[i];
                    break;
                }
            }
        }
        return result.toString();
    }
}

