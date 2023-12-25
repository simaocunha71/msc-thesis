/*
Given a positive integer N, return the total sum of its digits in binary.

Example
    For N = 1000, the sum of digits will be 1 the output should be "1".
    For N = 150, the sum of digits will be 6 the output should be "110".
    For N = 147, the sum of digits will be 12 the output should be "1100".

Variables:
    @N integer
         Constraints: 0 ≤ N ≤ 10000.
Output:
     a string of binary number
*/
#include<stdio.h>
#include<string>
using namespace std;
string solve(int N){
    int count = 0, sum = 0;
    while(N!=0){
        if((sum+1)%2 != 0)
            cout<<"1";
        else
            cout<<"0";
        sum += (N%2);
        N/=2;
    }
    return "";
}
int main(){
    int n = 0, res;
    cin >> n;
    res = solve(n);
    printf("\nSum of digits in binary is : %s",res.c_str());
    getchar();
    return 0;
}