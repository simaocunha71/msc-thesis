import java.util.*;
import java.lang.*;

class Solution {
    /**
    Write a function that takes a string and returns true if the string
    length is a prime number or false otherwise
    Examples
    primeLength("Hello") == true
    primeLength("abcdcba") == true
    primeLength("kittens") == true
    primeLength("orange") == false
     */
    public boolean primeLength(String string) {
        int count=0;
        for(int i=0;i<string.length();i++)
        {
            count++;
        }
        int count1=0;
        for(int i=2;i<=count;i++)
        {
            if(count%i==0)
            {
                count1=count1+1;
            }
        }
        if(count1==1)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}

B:
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Write a function that takes a string and returns true if the string
    length is a prime number or false otherwise
    Examples
    primeLength("Hello") == true
    primeLength("abcdcba") == true
    primeLength("kittens") == true
    primeLength("orange") == false
     */
    public boolean primeLength(String string) {
        int count=0;
        for(int i=0;i<string.length();i++)
        {
            count++;
        }
        if(count==1)
        {
            return true;
        }
        else if(count%2==0||count%3==0||count%5==0||count%7==0)
        {
            return false;
        }
        else
        {
            return true;
        }
    }
}

C:
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Write a function that takes a string and returns true if the string
    length is a prime number or false otherwise
    Examples
    primeLength("Hello