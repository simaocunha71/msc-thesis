    StringBuilder result = new StringBuilder();

    Map<Integer, String> map = new HashMap<>();
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

    for (Map.Entry<Integer, String> entry : map.entrySet()) {
        int key = entry.getKey();
        String value = entry.getValue();
        while (number >= key) {
            result.append(value);
            number -= key;
        }
    }
    return result.toString();
}
}



# Python

def intToMiniRoman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> intToMiniRoman(19) == "xix"
    >>> intToMiniRoman(152) == "clii"
    >>> intToMiniRoman(426) == "cdxxvi"
    """
    romans = (
        (1000, "m"),
        (900, "cm"),
        (500, "d"),
        (400, "cd"),
        (100, "c"),
        (90, "xc"),
        (50, "l"),
        (40, "xl"),
        (10, "x"),
        (9, "ix"),
        (5, "v"),
        (4, "iv"),
        (1, "i"),
