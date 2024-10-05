import java.util.*;

class Solution {
    public String intToMiniRoman(int number) {
        if (number <= 0) {
            return "";
        }
        String roman = "";
        while (number >= 1000) {
            roman += "m";
            number -= 1000;
        }
        if (number >= 900) {
            roman += "cm";
            number -= 900;
        }
        while (number >= 500) {
            roman += "d";
            number -= 500;
        }
        if (number >= 400) {
            roman += "cd";
            number -= 400;
        }
        while (number >= 100) {
            roman += "c";
            number -= 100;
        }
        if (number >= 90) {
            roman += "xc";
            number -= 90;
        }
        while (number >= 50) {
            roman += "l";
            number -= 50;
        }
        if (number >= 40) {
            roman += "xl";
            number -= 40;
        }
        while (number >= 10) {
            roman += "x";
            number -= 10;
        }
        if (number >= 9) {
            roman += "ix";
            number -= 9;
        }
        while (number >= 5) {
            roman += "v";
            number -= 5;
        }
        if (number >= 4) {
            roman += "iv";
            number -= 4;
        }
        while (number > 0) {
            roman += "i";
            number -= 1;
        }
        return roman;
    }
}


