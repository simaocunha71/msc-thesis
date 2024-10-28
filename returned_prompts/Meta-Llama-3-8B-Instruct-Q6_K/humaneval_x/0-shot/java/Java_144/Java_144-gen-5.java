    public boolean simplify(String x, String n) {
        int a = getNumerator(x);
        int b = getDenominator(x);
        int c = getNumerator(n);
        int d = getDenominator(n);

        int gcd = getGCD(Math.max(a, c), Math.max(b, d));
        int numerator = a * d / gcd;
        int denominator = b * c / gcd;

        return (numerator == denominator) ? true : false;
    }

    private int getNumerator(String s) {
        return Integer.parseInt(s.split("/")[0]);
    }

    private int getDenominator(String s) {
        return Integer.parseInt(s.split("/")[1]);
    }

    private int getGCD(int a, int b) {
        if (b == 0) {
            return a;
        }
        return getGCD(b, a % b);
    }
}  //package com.interview;

//import java.util.*; // Remove this line
//import java.lang.*; // Remove this line

// Your code here
//public class Solution {
//    public boolean simplify(String x, String n) {
//        int a = getNumerator(x);
//        int b = getDenominator(x);
//        int c = getNumerator(n);
//        int d = getDenominator(n);
//        
//        int gcd = getGCD(Math.max(a, c), Math.max(b, d));
//        int numerator = a * d / gcd;
//        int denominator = b * c / gcd;
//        
//        return (numerator == denominator) ? true : false;
//    }
//    
//    private int getNumerator(String s) {
//        return Integer.parseInt(s.split("/")[0]);
//    }
//    
//    private int getDenominator(String s) {
//        return Integer.parseInt(s.split("/")[1]);
//    }
//    
//    private int getGCD(int a, int b) {
//        if (b == 0) {
//            return a;
//        }
//        return getGCD(b, a % b);
//    }
//}

Explanation:
This solution first extracts the numerators and denominators from the input strings using the getNumerator and getDenominator methods. It then calculates the greatest common divisor (GCD) of the maximum of the two numerators and the maximum of the two denominators using the getGCD method.

The GCD is used to