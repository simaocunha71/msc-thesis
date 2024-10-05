        Map<Integer, String> romanMap = new HashMap<>();
        romanMap.put(1000, "m");
        romanMap.put(900, "cm");
        romanMap.put(500, "d");
        romanMap.put(400, "cd");
        romanMap.put(100, "c");
        romanMap.put(90, "xc");
        romanMap.put(50, "l");
        romanMap.put(40, "xl");
        romanMap.put(10, "x");
        romanMap.put(9, "ix");
        romanMap.put(5, "v");
        romanMap.put(4, "iv");
        romanMap.put(1, "i");

        StringBuilder roman = new StringBuilder();
        for (Map.Entry<Integer, String> entry : romanMap.entrySet()) {
            while (number >= entry.getKey()) {
                roman.append(entry.getValue());
                number -= entry.getKey();
            }
        }
        return roman.toString().toLowerCase();
    }
}

