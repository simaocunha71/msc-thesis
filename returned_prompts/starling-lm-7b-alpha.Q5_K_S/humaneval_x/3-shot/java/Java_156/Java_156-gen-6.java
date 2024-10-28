        if (number == 0) return "";
        HashMap<Integer, String> m = new HashMap<>();
        m.put(1000, "m");
        m.put(900, "cm");
        m.put(500, "d");
        m.put(400, "cd");
        m.put(100, "c");
        m.put(90, "xc");
        m.put(50, "l");
        m.put(40, "xl");
        m.put(10, "x");
        m.put(9, "ix");
        m.put(5, "v");
        m.put(4, "iv");
        m.put(1, "i");

        String result = "";
        for (Map.Entry<Integer, String> e : m.entrySet()) {
            int key = e.getKey();
            String value = e.getValue();
            while (key <= number) {
                result += value;
                number -= key;
            }
        }
        return result;
    }
}

