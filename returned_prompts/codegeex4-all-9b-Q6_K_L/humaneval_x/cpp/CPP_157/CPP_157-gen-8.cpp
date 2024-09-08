/*
Given a number n, write a function that returns the sum of all the squares of
all the integers from 1 to n, inclusive.
Example:
sum_squares(3) = 14
since 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14
sum_squares(5) = 55
since 1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 1 + 4 + 9 + 16 + 25 = 55
*/

int sum_squares(int n){
    int sum = 0;
    for(int i = 1;i <= n;i++){
        sum += pow(i,2);
    }
    return sum;
}

