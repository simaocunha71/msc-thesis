        // Decimal to roman number mapping
        Map<Integer, String> roman_map = new HashMap<Integer, String>() {{
            put(1000, "m");
            put(900, "cm");
            put(500, "d");
            put(400, "cd");
            put(100, "c");
            put(90, "xc");
            put(50, "l");
            put(40, "xl");
            put(10, "x");
            put(9, "ix");
            put(5, "v");
            put(4, "iv");
            put(1, "i");
        }};

        String result = "";
        for (Map.Entry<Integer, String> entry : roman_map.entrySet()) {
            while (number >= entry.getKey()) {
                number -= entry.getKey();
                result += entry.getValue();
            }
        }
        return result;
    }
}

