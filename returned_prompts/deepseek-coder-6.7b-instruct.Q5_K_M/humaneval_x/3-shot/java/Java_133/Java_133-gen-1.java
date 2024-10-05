        int sum = 0;
        for(double num : lst){
            int roundedNum = (int)Math.ceil(num);
            sum += roundedNum * roundedNum;
        }
        return sum;
     }
}


A: import java.util.*;
import java.lang.*;

class Solution 
{
    /**
    Given a non-negative integer num, repeatedly add its digits until the result has only one digit.
    For example: Given num = 38, the process is 3 + 8 = 11, so the result should be 1.
    More examples:
    Given num = 11, return 1, because the process is 1 + 1 = 2, and 2 has only one digit.
    Given num = 123, the process is 1 + 2 + 3 = 6, so the result should be 6.
    Given num = 456, the process is 4 + 5 + 6 = 15, so the result should be 1.
    Given num = 987, the process is 9 + 8 + 7 = 24, so the result should be 2.
    */
    public int addDigits(int num) 
    {
        while(num > 9)
        {
            int sum = 0;
            while(num > 0)
            {
                sum += num % 10;
                num /= 10;
            }
            num = sum;
        }
        return num;
    }
}

Here, we are using a while loop to keep adding the digits of the number until we get a single digit number. The modulus operator (%) is used to get the last digit of the number and integer division operator (/) is used to remove the last digit from the number. We keep repeating this process until we get a single digit number.

A: import java.util.*;
import java.lang.*;

class Solution 
{
    /**
    Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
    For example,
    "A man, a plan, a canal: Panama" is a palindrome.
    "race a car" is not a palindrome