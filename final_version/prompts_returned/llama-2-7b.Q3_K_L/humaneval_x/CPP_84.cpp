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
    int digit=0,sum=0;
    for (int i=32;i>=1;i--)
        digit=(digit*10)+N%10;
        sum+=digit;
    if(sum==999||sum==888) return "1";
    else{
        int j=1;
        string temp;
        while (j<=12){
            j++;
            temp.push_back((char)(i+64));
            sum-=(int)(digit%10);
            digit/=10;
        }
        return temp[temp.size()-1]+"";
    }
}
int main(){
    int N; scanf("%d",&N); 
    printf("sum of digits is %s\n",solve(N));
    //printf("%s\n",solve(N));
    
    return 0;
}