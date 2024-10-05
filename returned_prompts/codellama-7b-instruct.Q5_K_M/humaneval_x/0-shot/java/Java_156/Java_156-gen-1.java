        String roman = "";
        while (number > 0) {
            if (number >= 1000) {
                roman = "M" + roman;
                number -= 1000;
            } else if (number >= 900) {
                roman = "cm" + roman;
                number -= 900;
            } else if (number >= 500) {
                roman = "d" + roman;
                number -= 500;
            } else if (number >= 400) {
                roman = "cd" + roman;
                number -= 400;
            } else if (number >= 100) {
                roman = "c" + roman;
                number -= 100;
            } else if (number >= 90) {
                roman = "xc" + roman;
                number -= 90;
            } else if (number >= 50) {
                roman = "l" + roman;
                number -= 50;
            } else if (number >= 40) {
                roman = "xl" + roman;
                number -= 40;
            } else if (number >= 10) {
                roman = "x" + roman;
                number -= 10;
            } else if (number >= 9) {
                roman = "ix" + roman;
                number -= 9;
            } else if (number >= 5) {
                roman = "v" + roman;
                number -= 5;
            } else if (number >= 4) {
                roman = "iv" + roman;
                number -= 4;
            } else if (number >= 1) {
                roman = "i" + roman;
                number -= 1;
            }
        }
        return roman;
    }

    public static void main(String[] args) {
        System.out.println(new Solution().intToMiniRoman(19));
        System.out.println(new Solution().intToMiniRoman(152));
        System.out.println(new Solution().intToMiniRoman(426));