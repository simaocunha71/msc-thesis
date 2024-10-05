    int count = 0;

B:
    if(n < 1){
        return 0;
    }

C:
    if(n == 1){
        return 2;
    }

D:
    for(int i = 1; i < n; i++){
        count += 2*9;
    }

E:
    return count + 2;
}

int main(){
    int num;
    printf("Enter a positive integer: ");
    scanf("%d", &num);
    printf("The count of n-digit positive integers that start or end with 1 is: %d\n", starts_one_ends(num));
    return 0;
}
*/

// A: Start by initializing a variable count to 0.
// B: If the input number is less than 1, return 0 as there are no numbers that start or end with 1.
// C: If the input number is 1, return 2 as there are only 2 one-digit numbers that start or end with 1.
// D: For each digit from 2 to n, calculate the count of n-digit numbers that start or end with 1 and add it to count. The count of n-digit numbers that start or end with 1 is 2 * 9^(n-1), where 9^(n-1) is the count of (n-1)-digit numbers.
// E: Finally, add 2 to count to account for the two one-digit numbers that start or end with 1.

// The time complexity of this code is O(n) and the space complexity is O(1).

// Note: The function starts_one_ends(int n) is not a correct solution to the problem as it does not consider the cases where the number has 1 as its second last digit or 1 as its second digit.

// The correct code is as follows:

#include<stdio.h>
using namespace std;
int starts_one_ends(int n){

    if(n < 1){
        return 0;
    }

    if(n == 1){
        return 2;
    }

    int count = 0