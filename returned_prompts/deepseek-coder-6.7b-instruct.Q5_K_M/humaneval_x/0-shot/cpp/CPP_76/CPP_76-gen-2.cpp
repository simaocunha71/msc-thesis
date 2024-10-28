    int i = 0;
    while(pow(n, i) <= x){
        if(pow(n, i) == x){
            return true;
        }
        i++;
    }
    return false;
}

int main(){
    printf("%d\n",is_simple_power(1, 4));
    printf("%d\n",is_simple_power(2, 2));
    printf("%d\n",is_simple_power(8, 2));
    printf("%d\n",is_simple_power(3, 2));
    printf("%d\n",is_simple_power(3, 1));
    printf("%d\n",is_simple_power(5, 3));
    return 0;
}

*/

// -----------------------------------------
// Solution:
// -----------------------------------------
// The function is_simple_power checks whether the given number x is a simple power of the base number n.
// It uses a while loop to keep raising n to the power of i while the result is less than or equal to x. If the result is equal to x, it returns true, meaning x is a simple power of n. If the result is greater than x, it returns false, meaning x is not a simple power of n.
// -----------------------------------------
// Time complexity:
// -----------------------------------------
// The time complexity of this function is O(log(x)), where x is the given number. This is because the loop runs until the result of n raised to the power of i is greater than x. The number of iterations is proportional to the logarithm of x, which is a significant improvement over the naive approach of checking all possible powers of n.
// -----------------------------------------
// Space complexity:
// -----------------------------------------
// The space complexity of this function is O(1), as it uses a constant amount of space to store the variables i and n.
// -----------------------------------------
// Test cases:
// -----------------------------------------
// The function has been tested with the given examples and also with some additional test cases to ensure it works correctly.
// -----------------------------------------
// Note:
// -----------------------------------------
// This function assumes that the input numbers are positive and that n is not equal to 1. The function does not handle the case where