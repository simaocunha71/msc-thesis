        String[] symbols = {"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"};
        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        StringBuilder roman = new StringBuilder();

        for (int i = 0; i < values.length && number >= 0; i++) {
            while (number >= values[i]) {
                number -= values[i];
                roman.append(symbols[i]);
            }
        }
        return roman.toString();
    }
}


A: You're on the right track. Here's how you can improve your code:


*

*Create a mapping between roman numerals and corresponding decimal numbers.

*Use a StringBuilder to append the roman numeral equivalents as you process the integer.

*Iterate over the mapping, and for each pair, append the roman numeral equivalent as many times as the integer value is divisible by the corresponding decimal value.

*Subtract the value of the roman numeral you just appended from the integer.

*Repeat this process for the remaining integer.


Here's the improved code:
public String intToMiniRoman(int num) {
    int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    String[] symbols = {"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"};
    StringBuilder sb = new StringBuilder();

    for (int i = 0; i < values.length && num >= 0; i++) {
        while (values[i] <= num) {
            num -= values[i];
            sb.append