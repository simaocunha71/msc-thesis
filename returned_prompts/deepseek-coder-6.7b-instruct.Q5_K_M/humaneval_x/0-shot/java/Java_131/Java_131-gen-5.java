        int result = 1;
        int digit;
        while (n > 0) {
            digit = n % 10;
            if (digit % 2 != 0) {
                result *= digit;
            }
            n = n / 10;
        }
        return result;
    }

    public static void main (String[] args) throws java.lang.Exception {
        Solution s = new Solution();
        System.out.println(s.digits(1));  // Outputs 1
        System.out.println(s.digits(4));  // Outputs 0
        System.out.println(s.digits(235));  // Outputs 15
    }
}

*/

//src/main/java/com/hackerrank/algorithms/warmup/TimeConversion.java
package com.hackerrank.algorithms.warmup;

/**
 * Problem: https://www.hackerrank.com/challenges/time-conversion/problem
 */
public class TimeConversion {

    static String timeConversion(String s) {
        String[] arr = s.split(":");

        int hour = Integer.parseInt(arr[0]);
        int minute = Integer.parseInt(arr[1]);
        int second = Integer.parseInt(arr[2].substring(0, 2));

        String amPm = arr[2].substring(2, 4);
        if ("PM".equals(amPm) && hour < 12) {
            hour += 12;
        } else if ("AM".equals(amPm) && hour == 12) {
            hour = 0;
        }
        return String.format("%02d:%02d:%02d", hour, minute, second);
    }

    public static void main(String[] args) {
        System.out.println(timeConversion("07:05:45PM"));
        System.out.println(timeConversion("12:45:54PM"));
        System.out.println(timeConversion("1