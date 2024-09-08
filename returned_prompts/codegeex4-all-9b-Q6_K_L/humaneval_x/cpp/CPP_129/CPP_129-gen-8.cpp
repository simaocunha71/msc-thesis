/*
You are given an array of n integers a[1], a[2], ..., a[n] and an integer k.
You are allowed to perform any number of operations on the array. 
In each operation, you can select a subarray (continuous segment of the array) 
with length at least 2 and swap the first and the last elements of the subarray.
For example, if you have an array a = {2, 1, 3, 5, 4} and you select the subarray 
a[2:4] = {3, 5, 4}, then after swapping the first and the last elements of the 
subarray, you get a = {2, 1, 4, 5, 3}.
Find the minimum number of operations needed to sort the array in non-decreasing 
order if you are allowed to perform at most k such operations.

Examples:

    Input: a = {1, 2, 3, 4, 5}, k = 1
    Output: 0

    Input: a = {5, 4, 3, 2, 1}, k = 4
    Output: 1

    Input: a = {5, 1, 4, 3, 2}, k = 1
    Output: 2
*/
#include<stdio.h>
#include<vector>
using namespace std;
int minOps(vector<int> a, int k){

B:
/*
You are given an array of n integers a[1], a[2], ..., a[n] and an integer k.
You are allowed to perform any number of operations on the array. 
In each operation, you can select a subarray (continuous segment of the array) 
with length at least 2 and swap the first and the last elements of the subarray.
For example, if you have an array a = {2, 1, 3, 5, 4} and you select the subarray 
a[2:4] = {3, 5, 4}, then after swapping the first and the last elements of the 
subarray, you get a = {2, 1, 4, 5, 3}.
Find the minimum number of operations needed to sort the array in non-decreasing 
order if you are allowed to perform at most k such operations.

Examples:

    Input: a = {1, 2, 3,