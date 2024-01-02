import java.util.*;
import java.lang.*;

class Solution {
    /**
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
     */
    public List<Integer> factorize(int n) {
        ArrayList<Integer> primeFactors = new ArrayList<>();
        
        while (n!=1){
            int currentDivisor;
            
            if((currentDivisor=Math.sqrt(n)) <= 20){
                // if n is less than square root of 20, we do not need to use
                // the modular inverse because it will be smaller than sqrt(n) and prime
                
                int divisor = (int)(Math.pow((double)currentDivisor,(double)1/2))-1;
                n %= divisor;
            } else {
                int modInverse = Math.pow((double)currentDivisor, 0.5);
                
                // if n is greater than square root of 20 we use the modified inverse in order to find out which number is a prime factor
                while (currentDivisor !=1){
                    int tempDivisor = (int)Math.pow(modInverse, currentDivisor);
                    n %= tempDivisor;
                    currentDivisor--;     // decrease by 1 everytime divisor becomes equal to sqrt(n)/2
                }   // while loop for modified inverse because it is a prime number we only need to divide by it once since the quotient will be zero and this will result in an infinite recurrence
                
                currentDivisor--;
                n %= currentDivisor;
            } 
            if (n !=1){
                for(int i = 2;i<=currentDivisor;i++){
                    if((