        int largestPrime = -1;
        for(int i = 0; i < lst.size(); i++){
            if(isPrime(lst.get(i)) && lst.get(i) > largestPrime){
                largestPrime = lst.get(i);
            }
        }
        return sumOfDigits(largestPrime);
    }

    private boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    private int sumOfDigits(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}

The function "isPrime" checks whether a given number is prime or not. The function "sumOfDigits" calculates the sum of digits of a given number.
The function "skjkasdkd" finds the largest prime number in the input list and returns the sum of its digits.


A: The code you've posted is almost correct, but there is a small typo in your question. The name of your function is "skjkasdkd", but it seems that you want to find the largest prime number.
Here is the corrected code:
import java.util.*;
import java.lang.*;

class Solution {
    public int largestPrimeAndDigitSum(List<Integer> lst) {
        int largestPrime = -1;
        for (int i = 0; i < lst.size(); i++) {
            if (isPrime(lst.get(i)) && lst.get(i) > largestPrime) {
                largestPrime = lst.get(i);
            }
        }
        return sumOfDigits(largestPrime);
    }

    private boolean isPrime(int num) {
        if (num <= 1) {
