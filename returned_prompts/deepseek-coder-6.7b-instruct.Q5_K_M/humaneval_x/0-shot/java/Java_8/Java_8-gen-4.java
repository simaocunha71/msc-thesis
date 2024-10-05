        int sum = 0;
        int product = 1;
        for(int num : numbers){
            sum += num;
            product *= num;
        }
        return Arrays.asList(sum, product);
    }
}


A: Your code is correct, but you are missing import statement for Arrays.asList. It should be 
import java.util.Arrays;

And also, you should consider to throw an exception when the input is null.
import java.util.*;
import java.lang.*;

class Solution  {
    public List<Integer> sumProduct(List<Integer> numbers)  {
        if(numbers == null) throw new IllegalArgumentException("Null not allowed");

        int sum = 0;
        int product = 1;
        for(int num : numbers){
            sum += num;
            product *= num;
        }
        return Arrays.asList(sum, product);
    }
}

This way you can avoid NullPointerException when you call sumProduct method with null argument.

A: Your code is correct. You've just missed the import statement for Arrays.asList(). 
Here is the correct code:
import java.util.*;
import java.lang.*;
import java.util.Arrays;

class Solution {
    public List<Integer> sumProduct(List<Integer> numbers) {
        int sum = 0;
        int product = 1;
        for(int num : numbers){
            sum += num;
            product *= num;
        }
        return Arrays.asList(sum, product);
    }
}

This code will return a list of two integers. The first one is the sum of all numbers in the input list, and the second one is the product of all numbers. If the input list is empty, it will return [0, 1].

A: The code you've provided is correct. You've just missed the import statement for Arrays.asList(). Here's the corrected code:
import java.util.*;
import java.lang.*;
import java.util.Arrays;

class Solution {
    public List<Integer> sumProduct(List<Integer> numbers) {
        int sum