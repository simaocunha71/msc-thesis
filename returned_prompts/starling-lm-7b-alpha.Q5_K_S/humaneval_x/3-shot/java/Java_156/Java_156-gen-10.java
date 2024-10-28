        int[] minis = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] minis_str = {"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"};

        String result = "";
        for (int i = 0; i < minis.length; i++) {
            while (number >= minis[i]) {
                result += minis_str[i];
                number -= minis[i];
            }
        }
        return result;
    }
}

