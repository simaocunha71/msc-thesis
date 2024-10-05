        String[] roman = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        int[] arabic = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};

        StringBuilder result = new StringBuilder();

        for (int i = 0; i < arabic.length; i++) {
            while (number >= arabic[i]) {
                number -= arabic[i];
                result.append(roman[i]);
            }
        }

        return result.toString().toLowerCase();
    }
}