/*
For a given number n, find the largest number that divides n evenly, smaller than n
>>> largest_divisor(15)
5
*/
#include<iostream>
using namespace std;
int largest_divisor(int n){
    int i=1;
    for(i=1;i<n;i++){
        if(n%i==0){
            return i;
        }
    }
    return -1;
}

