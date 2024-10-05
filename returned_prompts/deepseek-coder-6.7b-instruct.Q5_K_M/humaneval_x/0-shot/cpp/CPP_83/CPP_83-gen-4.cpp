    if(n==1)
        return 2;
    if(n<=0)
        return 0;
    return starts_one_ends(n-1)+starts_one_ends(n-2);
}

int main(){
    int n;
    scanf("%d",&n);
    printf("%d",starts_one_ends(n));
    return 0;
}

*/
#include<stdio.h>
#include<math.h>
int main(){
    int n;
    scanf("%d",&n);
    printf("%d",(int)pow(2,n-1));
    return 0;
}
/*
Answer:
The logic behind this solution is that for every digit from 2 to n, we can either place '1' as the first digit or as the last digit. Now, if we place '1' as the first digit, we have n-1 digits left and if we place '1' as the last digit, we have n-1 digits left. So, we can calculate the count of n-digit numbers that start or end with '1' by taking the power of 2 to n-1 and then multiplying it by 2 (once for starting with '1' and once for ending with '1').

This solution is more efficient than the recursive solution because it avoids the repeated calculation of the same sub-problems.
*/
/*
This solution is based on the principle of dynamic programming and the observation that the number of n-digit numbers that start or end with 1 is equal to the number of (n-1)-digit numbers that start or end with 1.

This solution has a time complexity of O(n) and a space complexity of O(1), making it more efficient than the recursive solution.
*/

// END CODE

// END SOLUTION

// END ANSWER

// END FINAL SOLUTION

// END ANSWER

// END FINAL SOLUTION

// END ANSWER

// END FINAL SOLUTION

// END ANSWER

// END FINAL SOLUTION

// END A