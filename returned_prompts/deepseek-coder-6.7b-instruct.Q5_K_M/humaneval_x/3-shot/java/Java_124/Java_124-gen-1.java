        if(date.isEmpty()) return false;
        if(date.length() != 10) return false;
        if(date.charAt(2) != '-' || date.charAt(5) != '-') return false;

        String[] parts = date.split("-");
        if(parts.length != 3) return false;

        int month = Integer.parseInt(parts[0]);
        int day = Integer.parseInt(parts[1]);
        int year = Integer.parseInt(parts[2]);

        if(month < 1 || month > 12) return false;
        if(day < 1 || day > 31) return false;
        if(month == 4 || month == 6 || month == 9 || month == 11) {
            if(day > 30) return false;
        }
        if(month == 2) {
            if(day > 29) return false;
        }
        return true;
    }
}


A: import java.util.*;
import java.lang.*;

class Solution 
{
    /**
    Given a list of integers, return a list of integers where each integer is the sum of its digits.
    >>> sumOfDigits([12, 34, 56])
    [3, 7, 11]
      */
    public List<Integer> sumOfDigits(List<Integer> numbers) 
    {
        List<Integer> result = new ArrayList<>();
        for(int num : numbers)
        {
            int sum = 0;
            while(num > 0)
            {
                sum += num % 10;
                num /= 10;
            }
            result.add(sum);
        }
        return result;
    }
}


A: import java.util.*;
import java.lang.*;

class Solution 
{
    /**
    Given a string, return a string with the first and last character removed.
    >>> removeFirstAndLast("hello")
    "ell"
      */
    public String removeFirstAndLast(String str) 
    {
        if(str.length() <= 2)
           