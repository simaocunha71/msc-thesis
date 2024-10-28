        String[] romanNumerals = new String[] { "m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i" };
        int[] romanValues = new int[] { 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 };
        String result = "";

        for (int i = 0; i < romanValues.length; i++) {
            while (number >= romanValues[i]) {
                number -= romanValues[i];
                result += romanNumerals[i];
            }
        }
        return result;

    }
}

