        String[] intToMiniRoman = new String[]{"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"};
        int[] intToMiniRomanValues = new int[]{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String result = "";

        for (int i = 0; i < intToMiniRomanValues.length; i++) {
            while (number >= intToMiniRomanValues[i]) {
                number -= intToMiniRomanValues[i];
                result += intToMiniRoman[i];
            }
        }

        return result;
    }
}

