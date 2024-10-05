/*
Write a function that receives a vector of integers and returns the first positive
integer in the vector. If no positive integer is found, return None.
>>> first_positive({})

>>> first_positive({-1, -2, -3})
None
>>> first_positive({0, 1, 2})
1
*/
#include<stdio.h>
#include<vector>
using namespace std;
int first_positive(vector<int> nums){

