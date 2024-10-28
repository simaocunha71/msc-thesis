    public String intToMiniRoman(int number) {
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
            int value = entry.getKey();
            String symbol = entry.getValue();

            while (number >= value) {
                roman.append(symbol);
                number -= value;
            }
        }

        return roman.toString().toLowerCase();
    }  



Explanation:
The `intToMiniRoman` function converts an integer to its roman numeral equivalent. It uses a HashMap to store the roman numerals and their corresponding integer values. The function iterates through the map, appending the roman numeral to a StringBuilder for each integer value that is greater than or equal to the current value. The result is the roman numeral equivalent of the input integer as a string, in lowercase.

The function handles the following cases:
- 1000: M
- 900: CM
- 500: D
- 400: CD
- 100: C
- 90: XC
- 50: L
- 40: XL
- 10: X
- 9: IX
- 5: V
- 4: IV
- 1: I

The function returns the roman numeral equivalent as a string, in lowercase. For example, `intToMiniRoman(19)` returns "xix", `intToMiniRoman(152)` returns "clii", and `intToMiniRoman(426)` returns "cdxxvi".  



Note: This function assumes that the input integer is within the range 1 to 1000. If the input integer is outside this range, the function may not produce the correct result.  



This function is case-insensitive, meaning it returns the roman numeral equivalent in lowercase, regardless of