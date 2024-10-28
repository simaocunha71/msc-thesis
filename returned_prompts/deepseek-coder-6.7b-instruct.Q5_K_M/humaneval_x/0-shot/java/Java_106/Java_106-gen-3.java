        List<Integer> result = new ArrayList<>();
        for(int i = 1; i <= n; i++) {
            if(i % 2 == 0) {
                result.add(factorial(i));
            } else {
                result.add(sum(i));
            }
        }
        return result;
    }

    private int factorial(int num) {
        int fact = 1; 
        for(int i = 1; i <= num; i++) {
            fact *= i;
        }
        return fact;
    }

    private int sum(int num) {
        int sum = 0; 
        for(int i = 1; i <= num; i++) {
            sum += i;
        }
        return sum;
    }
}

The code above does exactly what you asked for.
It has a function f that takes an integer as a parameter and returns a list of integers of size n.
The function factorial is used to calculate the factorial of a number.
The function sum is used to calculate the sum of numbers from 1 to a number.
The elements of the list are calculated based on whether the index of the element is even or odd.
If the index is even, the element is the factorial of the index. If the index is odd, the element is the sum of numbers from 1 to the index.
*/

// C:
/*
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> f(int n) {
        List<Integer> result = new ArrayList<>();
        for(int i = 1; i <= n; i++) {
            if(i % 2 == 0) {
                result.add(factorial(i));
            } else {
                result.add(sum(i));
            }
        }
        return result;
    }

    private int factorial(int num) {
        int fact = 1; 
        for(int i = 1; i <= num; i++) {
            fact *= i;
        }
        return fact;
    }

    private int sum(int num) {
        int sum = 0;