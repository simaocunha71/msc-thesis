        // Create a map to store the values
        Map<Integer, String> map = new HashMap<>();
        map.put(1, "i");
        map.put(4, "iv");
        map.put(5, "v");
        map.put(9, "ix");
        map.put(10, "x");
        map.put(40, "xl");
        map.put(50, "l");
        map.put(90, "xc");
        map.put(100, "c");
        map.put(400, "cd");
        map.put(500, "d");
        map.put(900, "cm");
        map.put(1000, "m");

        // Initialize result as empty string
        String result = "";

        // Loop from the biggest to the smallest
        for (int i = 1000; i > 0; i /= 10) {
            while (number >= i) {
                number -= i;
                result += map.get(i);
            }
        }

        return result;
    }
}

