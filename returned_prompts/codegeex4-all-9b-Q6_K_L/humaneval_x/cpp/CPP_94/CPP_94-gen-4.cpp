/*
You are given a vector of integers.
You need to find the largest prime value and return the sum of its digits.

Examples:
For lst = {0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3} the output should be 10
For lst = {1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1} the output should be 25
For lst = {1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3} the output should be 13
For lst = {0,724,32,71,99,32,6,0,5,91,83,0,5,6} the output should be 11
For lst = {0,81,12,3,1,21} the output should be 3
For lst = {0,8,1,2,1,7} the output should be 7
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
int skjkasdkd(vector<int> lst){
int max=0;
for(int i=0;i<lst.size();i++){
if(lst[i]>max){
max=lst[i];
}
}
for(int i=0;i<lst.size();i++){
if(lst[i]==max){
}
}
}
int main(){
int a;
printf("input a:");
scanf("%d",&a);
vector<int> lst;
for(int i=0;i<a;i++){
int c;
scanf("%d",&c);
lst.push_back(c);
}
printf("%d",skjkasdkd(lst));
return 0;
}

Here is a solution for the problem. This solution includes a helper function 'isPrime' to check if a number is prime or not and a helper function 'sumOfDigits' to calculate the sum of digits of a number.

```cpp
#include<iostream>
#include<vector>
#include<string>
using namespace std;

bool isPrime(int n) {
    if (n <= 1)
        return false;
    if (n <= 3)
        return true;

    if (n % 2 == 0 || n