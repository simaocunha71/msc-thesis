        Map<Integer, String> roman_map = new HashMap<>();
        roman_map.put(1000, "m");
        roman_map.put(900, "cm");
        roman_map.put(500, "d");
        roman_map.put(400, "cd");
        roman_map.put(100, "c");
        roman_map.put(90, "xc");
        roman_map.put(50, "l");
        roman_map.put(40, "xl");
        roman_map.put(10, "x");
        roman_map.put(9, "ix");
        roman_map.put(5, "v");
        roman_map.put(4, "iv");
        roman_map.put(1, "i");

        List<String> mini_roman_list = new ArrayList<>();
        while (number > 0) {
            for (int key : roman_map.keySet()) {
                if (number >= key) {
                    mini_roman_list.add(roman_map.get(key));
                    number -= key;
                }
            }
        }
        return String.join("", mini_roman_list);
    }
}

