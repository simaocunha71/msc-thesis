    int i = 0;
    while(true){
        int pow_val = pow(n, i);
        if (pow_val == x)
            return true;
        if (pow_val > x)
            return false;
        i++;
    }
}

int main(){
    printf("%d\n", is_simple_power(1, 4));
    printf("%d\n", is_simple_power(2, 2));
    printf("%d\n", is_simple_power(8, 2));
    printf("%d\n", is_simple_power(3, 2));
    printf("%d\n", is_simple_power(3, 1));
    printf("%d\n", is_simple_power(5, 3));
    return 0;
}

/*
This code is written in C++. It works by using a while loop to keep raising the power of n and checking if it equals x. If it equals x, the function returns true. If it is greater than x, the function returns false, indicating that x is not a simple power of n. The loop continues until x is reached or exceeded.
*/


A: Your function is correct, but you are using pow function from math.h library. You can also solve this problem by using a loop that multiplies the base number by itself for each iteration.
Here is the solution in Python:

def is_simple_power(x, n):
    if n == 1:
        return x == 1
    base = n
    while base <= x:
        if base == x:
            return True
        base *= n
    return False

This function works by initializing the base to n and then in a loop, it multiplies the base by n until the base is greater than x. If at any point the base equals x, the function returns True. If the loop completes without finding a match, the function returns False.

Note: This code assumes that n and x are both positive integers. If x can be zero, you should add an additional check at the start of the function to return False if x is zero.
*/

A: Here is the code in Java:

public class Main {
    public static void main(String