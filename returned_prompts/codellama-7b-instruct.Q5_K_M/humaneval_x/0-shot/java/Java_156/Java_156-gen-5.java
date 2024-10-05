import java.util.*;

class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        in.close();

        System.out.println(intToMiniRoman(n));
    }

    /**
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> intToMiniRoman(19) == "xix"
    >>> intToMiniRoman(152) == "clii"
    >>> intToMiniRoman(426) == "cdxxvi"
     */
    public static String intToMiniRoman(int number) {
        String[] romanNumerals = { "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" };
        int[] arabicNumerals = { 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 };
        StringBuilder romanNumeral = new StringBuilder();
        for (int i = 0; i < arabicNumerals.length; i++) {
            while (number >= arabicNumerals[i]) {
                number -= arabicNumerals[i];
                romanNumeral.append(romanNumerals[i]);
            }
        }
        return romanNumeral.toString();
    }
}