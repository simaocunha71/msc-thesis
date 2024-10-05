public String intToMiniRoman(int number) {
    HashMap<Integer, String> map = new HashMap<>();
    map.put(1000, "m");
    map.put(900, "cm");
    map.put(500, "d");
    map.put(400, "cd");
    map.put(100, "c");
    map.put(90, "xc");
    map.put(50, "l");
    map.put(40, "xl");
    map.put(10, "x");
    map.put(9, "ix");
    map.put(5, "v");
    map.put(4, "iv");
    map.put(1, "i");

    StringBuilder sb = new StringBuilder();
    for (Map.Entry<Integer, String> entry : map.entrySet()) {
        while (number >= entry.getKey()) {
            sb.append(entry.getValue());
            number -= entry.getKey();
        }
    }
    return sb.toString().toLowerCase();
}
