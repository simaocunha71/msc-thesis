import java.util.*;
import java.lang.*;

class Solution {
    /**
    Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100.
    Example:
    isMultiplyPrime(30) == true
    30 = 2 * 3 * 5
     */
    public boolean isMultiplyPrime(int a) {

        if(a<100)
        {
            int[] prime = new int[100];
            int count=0;
            for(int i=2;i<100;i++)
            {
                int check = i;
                for(int j=2;j<100;j++)
                {
                    if(check%j==0)
                    {
                        check++;
                        j--;
                    }
                    else
                    {
                        prime[count]=check;
                        count++;
                        break;
                    }
                }
            }
            for(int i=0;i<count;i++)
            {
                for(int j=0;j<count;j++)
                {
                    for(int k=0;k<count;k++)
                    {
                        if(prime[i]*prime[j]*prime[k]==a)
                        {
                            return true;
                        }
                    }
                }
            }
        }
        return false;
    }
}

