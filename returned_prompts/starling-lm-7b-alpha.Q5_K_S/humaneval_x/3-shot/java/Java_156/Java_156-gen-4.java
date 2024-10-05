        int[] numeral = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] roman = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

        StringBuilder result = new StringBuilder();
        for (int i = 0; i < numeral.length; i++) {
            while (number >= numeral[i]) {
                result.append(roman[i]);
                number -= numeral[i];
            }
        }
        return result.toString();
    }
}

