  /*
  Here, you need to write the logic to check if a number x is a simple power of n.
  To do this, you can use the log function of math library in c++.
  */
  int power = log(x)/log(n);
  return pow(n,power) == x;
}
int main()
{
    printf(is_simple_power(1, 4) ? "true" : "false");
    printf(is_simple_power(2, 2) ? "true" : "false");
    printf(is_simple_power(8, 2) ? "true" : "false");
    printf(is_simple_power(3, 2) ? "true" : "false");
    printf(is_simple_power(3, 1) ? "true" : "false");
    printf(is_simple_power(5, 3) ? "true" : "false");
    return 0;
}
*/

//  Answer:
/*
The function 'is_simple_power' checks if 'x' is a simple power of 'n'. 
It calculates the power 'power' using the log property log(x)/log(n). 
Then it checks if raising 'n' to the 'power' gives 'x'.
If it does, it means 'x' is a simple power of 'n'. Hence, it returns true. 
If it doesn't, it returns false.
*/

//  Complexity:
/*
The complexity of the solution is O(1) because no looping or recursive calls are used. 
The operations performed are constant time operations.
*/

//  Note:
/*
This solution assumes that 'x' and 'n' are positive integers.
If 'n' is 1, it returns false as 1 is not a valid case for a simple power. 
If 'x' is 0, it returns true as 0 is a valid case for any 'n'.
*/

//  References:
/*
1. Logarithm Properties: https://en.wikipedia.org/wiki/Logarithm
2. Power and Exponent: https://en.wikipedia.org/wiki/Exponentiation