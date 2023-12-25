/*
You are given a non-empty vector of positive integers. Return the greatest integer that is greater than 
zero, and has a frequency greater than or equal to the value of the integer itself. 
The frequency of an integer is the number of times it appears in the vector.
If no such a value exist, return -1.
Examples:
    search({4, 1, 2, 2, 3, 1}) == 2
    search({1, 2, 2, 3, 3, 3, 4, 4, 4}) == 3
    search({5, 5, 4, 4, 4}) == -1
*/
#include<stdio.h>
#include<vector>
using namespace std;
int search(vector<int> lst){
    int res=0;
    for (auto it = lst.cbegin();it!=lst.cend();++it) {   //iterate over every element of the vector
        if (*it > 0 && (*it).frequency()>=*it) {   //if we get a positive number from an iteration and that too is greater than zero, then it should be added to the resu lt
            ++res;
        } else if ((*it) <0) return -1;  //if the element at current position is negative then we are not going further into this loop
    }
    return (int)(res>0 ? res : -1);   //if positive number was found, return that value otherwise return -1.
}