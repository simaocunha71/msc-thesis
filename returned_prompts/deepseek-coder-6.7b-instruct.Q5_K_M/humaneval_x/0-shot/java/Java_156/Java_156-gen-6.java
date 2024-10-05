        // mapping of Roman to Integer
        Map<String, Integer> romanToInt = new HashMap<>();
        romanToInt.put("i", 1);
        romanToInt.put("v", 5);
        romanToInt.put("x", 10);
        romanToInt.put("l", 50);
        romanToInt.put("c", 100);
        romanToInt.put("d", 500);
        romanToInt.put("m", 1000);

        // mapping of Integer to Roman
        Map<Integer, String> intToRoman = new HashMap<>();
        intToRoman.put(1000, "m");
        intToRoman.put(900, "cm");
        intToRoman.put(500, "d");
        intToRoman.put(400, "cd");
        intToRoman.put(100, "c");
        intToRoman.put(90, "xc");
        intToRoman.put(50, "l");
        intToRoman.put(40, "xl");
        intToRoman.put(10, "x");
        intToRoman.put(9, "ix");
        intToRoman.put(5, "v");
        intToRoman.put(4, "iv");
        intToRoman.put(1, "i");

        // Converting the integer to roman
        String roman = "";
        int i = 1000;
        while (number != 0) {
            if (number >= i) {
                number -= i;
                roman += intToRoman.get(i);
            } else {
                i /= 10;
            }
        }

        // Converting the roman to mini roman
        String miniRoman = "";
        for (int j = 0; j < roman.length(); j++) {
            if (j > 0 && romanToInt.get(roman.substring(j, j + 1)) > romanToInt.get(roman.substring(j -