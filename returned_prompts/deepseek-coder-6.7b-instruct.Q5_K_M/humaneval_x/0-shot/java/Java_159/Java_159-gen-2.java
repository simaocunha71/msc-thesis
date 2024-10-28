        List<Integer> result = new ArrayList<>();
        if(need <= remaining){
            result.add(number + need);
            result.add(remaining - need);
        }else{
            result.add(number + remaining);
            result.add(0);
        }
        return result;
    }
}

This solution works by first checking if the carrots needed are less than or equal to the remaining carrots. If they are, we eat the needed number of carrots and subtract this from the remaining carrots. If there aren't enough carrots remaining, we eat all the remaining carrots and have no left over. The total number of carrots eaten is the original number of carrots eaten plus the amount eaten.

In terms of time complexity, this solution is O(1), because it always performs the same number of operations regardless of the input size. The space complexity is also O(1), because it always uses the same amount of space to store the result.
*/

//src/main/java/com/hackerrank/java/strings/JavaSubstringComparisons.java
package com.hackerrank.java.strings;

import java.util.Scanner;

public class JavaSubstringComparisons {

    public static String getSmallestAndLargest(String s, int k) {
        String smallest = s.substring(0, k);
        String largest = s.substring(0, k);

        for(int i = 1; i <= s.length() - k; i++){
            String substring = s.substring(i, i + k);
            if(smallest.compareTo(substring) > 0){
                smallest = substring;
            }
            if(largest.compareTo(substring) < 0){
                largest = substring;
            }
        }

        return smallest + "\n" + largest;
    }


    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();
      
        System.out.println(get