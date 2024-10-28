/*
Write a function that takes a vector of numbers as input and returns 
the number of elements in the vector that are greater than 10 and both 
first and last digits of a number are odd (1, 3, 5, 7, 9).
For example:
specialFilter({15, -73, 14, -15}) => 1 
specialFilter({33, -2, -3, 45, 21, 109}) => 2
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
int specialFilter(vector<int> nums){
    int count=0;
    for(auto i:nums){
        if(i>10){
            int first=i%10;
            int last=i/10%10;
            if(first==1 || first==3 || first==5 || first==7 || first==9 || last==1 || last==3 || last==5 || last==7 || last==9){
                count++;
            }
        }
    }
    return count;
}

