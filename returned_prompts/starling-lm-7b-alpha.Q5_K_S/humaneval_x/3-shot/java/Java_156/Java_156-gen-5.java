        int[] m = new int[]{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] r = new String[]{"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"};

        String result = "";
        for (int i = 0; i < m.length; i++) {
            while (number >= m[i]) {
                result += r[i];
                number -= m[i];
            }
        }
        return result;
    }
}

