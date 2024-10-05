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

        //Check if 3 is a factor
        if(a % 3 == 0){
            //Get the first prime factor
            int primeFactor1 = 3;
            //Get the second prime factor
            int primeFactor2 = 0;
            //Get the third prime factor
            int primeFactor3 = 0;
            //Check if 2 is a factor
            if(a % 2 == 0){
                //Get the first prime factor
                primeFactor1 = 2;
                //Get the second prime factor
                primeFactor2 = 2;
                //Get the third prime factor
                primeFactor3 = 3;
            }
            //Check if 5 is a factor
            else if(a % 5 == 0){
                //Get the first prime factor
                primeFactor1 = 5;
                //Get the second prime factor
                primeFactor2 = 3;
                //Get the third prime factor
                primeFactor3 = 2;
            }
            //Check if the product is correct
            if(a == (primeFactor1 * primeFactor2 * primeFactor3)){
                //Return true
                return true;
            }
            //Return false
            return false;
        }
        //Return false
        return false;
    }
}
